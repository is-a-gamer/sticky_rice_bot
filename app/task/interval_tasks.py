import datetime
import traceback
import aiohttp

from loguru import logger
from khl import Bot
from app.config.common import settings
from app.utils.channel_utils import update_channel_name_by_bot
from app.utils.playing_utils import set_playing_game_status_by_bot, BUSY_STATUS_GAME_ID, FREE_STATUS_GAME_ID
from app.voice_utils.container_async_handler import container_handler
from app.music.bilibili.search import BPROXY_API


async def clear_expired_candidates_cache():
    if settings.candidates_lock:
        return None
    else:
        settings.candidates_lock = True
        try:
            now = datetime.datetime.now()

            need_to_clear = []
            for this_user in settings.candidates_map:
                if now >= settings.candidates_map.get(this_user, {}).get("expire", now):
                    need_to_clear.append(this_user)

            for user_need_to_clear in need_to_clear:
                settings.candidates_map.pop(user_need_to_clear, None)
                logger.info(f"cache of user: {user_need_to_clear} is removed")

            settings.candidates_lock = False
            return None

        except Exception as e:
            settings.candidates_lock = False
            logger.error(
                f"error occurred in clearing expired candidates cache, error msg: {e}, traceback: {traceback.format_exc()}")


async def keep_bproxy_alive():
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(BPROXY_API) as r:
                resp_json = await r.json()
                logger.debug(resp_json)
                logger.info("bproxy is alive now")
    except Exception as e:
        logger.error(f"bproxy is not available, error msg: {e}, traceback: {traceback.format_exc()}")
        logger.error("bproxy is not alive now")


async def update_kanban_info(bot: Bot):
    try:
        if settings.kanban:
            status = "空闲" if len(settings.playqueue) == 0 else "繁忙"
            kanban_info = f"{settings.bot_name}: {status}"
            await update_channel_name_by_bot(bot=bot, channel_id=settings.kanban_channel, new_name=kanban_info)
            logger.info(f"kanban info is updated to {kanban_info} successfully")
    except Exception as e:
        logger.error(f"failed to update the kanban info, error msg: {e}, traceback: {traceback.format_exc()}")


async def update_playing_game_status(bot: Bot):
    try:
        game_status_id = FREE_STATUS_GAME_ID if len(settings.playqueue) == 0 else BUSY_STATUS_GAME_ID
        await set_playing_game_status_by_bot(bot=bot, game_id=game_status_id)
        logger.info(
            f"playing status is updated to {game_status_id} successfully.(busy is {BUSY_STATUS_GAME_ID}, free is {FREE_STATUS_GAME_ID})")
    except Exception as e:
        logger.error(f"failed to update playing status, error msg: {e}, traceback: {traceback.format_exc()}")


async def keep_bot_market_heart_beat():
    try:
        bot_market_url = "https://bot.gekj.net/api/v1/online.bot"

        if not settings.bot_market_heart_beat:
            logger.info(f"bot market heart beat switch is off, nothing happened")
        else:
            headers = {
                "uuid": settings.bot_market_uuid
            }
            async with aiohttp.ClientSession() as session:
                async with session.get(bot_market_url, headers=headers) as r:
                    resp_json = await r.json()
                    code = resp_json.get("code", -1)
                    msg = resp_json.get("msg", "no message received")
                    if code == 0:
                        logger.info(f"keep bot alive at bot market succeed, msg is {msg}")
                    else:
                        logger.error(f"failed to keep bot alive at bot market, msg is : {msg}")

    except Exception as e:
        logger.error(f"failed to keep bot alive at bot market, error msg: {e}, traceback: {traceback.format_exc()}")
