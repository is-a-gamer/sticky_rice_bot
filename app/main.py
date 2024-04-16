import json
import requests
from loguru import logger
from khl import Message, Bot
from khl.card import CardMessage
from app.bot import bot
from app.config.common import settings
from app.config import channel_bind
from app.config import ip_channel_bind
from app.utils.log_utils import loguru_decorator_factory as log
from app.utils.message_utils import update_cardmessage_by_bot
from app.task.interval_tasks import update_kanban_info, keep_bot_market_heart_beat

from app.tarkov.search import fetch_item_data_by_name, fetch_item_price_by_name, \
    fetch_hideout_all

import app.CardStorage as CS

__version__ = "0.8.0"

# logger
if settings.file_logger:
    logger.add(f"{settings.container_name}.log", rotation="1 week")

channel_bind.init()
ip_channel_bind.init()

# bot = Bot(token=settings.token)
gate = bot.client.gate


#########IP变更记录#############
# 用于存储上一次检测到的IP地址
previous_ip = None
def get_public_ip():
    try:
        # 使用一个可以返回你的公网IP地址的服务
        response = requests.get('https://api.ipify.org')
        if response.status_code == 200:
            return response.text
        else:
            print("Failed to retrieve IP address:", response.status_code)
    except Exception as e:
        print("Error retrieving IP address:", e)
    return None

###########IP变更记录#############

@log(command="ping")
@bot.command(name="ping")
async def ping(msg: Message):
    await msg.channel.send("コスモブルーフラッシュ！")
    logger.success(f"log_id: {msg.ctx.log_id} recieved")


@log(command="test_card")
@bot.command(name="test_card")
async def test_card(msg: Message):
    await msg.channel.send(CardMessage(CS.channel_card("user_name", "channel_name", "cu_time", "")))


@log(command="version")
@bot.command(name="version")
async def version(msg: Message):
    await msg.channel.send(f"Version number: {__version__}")


# @bot.command(name="help", aliases=["帮助", "文档", "手册", "说明", "示例", "命令", "?", "？"])
# @log(command="help")
async def help(msg: Message):
    await msg.channel.send(CardMessage(CS.HelpCard()))


############# 塔科夫开始 ###################

@log(command="tasearch")
@bot.command(name="tasearch", aliases=["塔搜索"])
async def tarkov_item_search(msg: Message, item_name):
    if not item_name:
        msg.channel.send("输入格式有误。\n正确格式为: /tasell {item_name} 或 /塔出售 {item_name}")
    else:
        d = await fetch_item_data_by_name(name=item_name)
        if len(d["data"]["items"]) == 0:
            raise Exception(f"未找到物品: {item_name}")
        taItemCard = CardMessage(*CS.taItemCard(d["data"]["items"]))
        await msg.channel.send(taItemCard)


@log(command="taprice")
@bot.command(name="taprice", aliases=["tapick", "塔价格"])
async def ta_price(msg: Message, item_name: str = ""):
    if not item_name:
        raise Exception("输入格式有误。\n正确格式为: /taprice {编号} 或 /塔价格 {编号}")
    else:
        data = await fetch_item_price_by_name(item_name)
        c = CardMessage(*CS.taItemPriceCard(data["data"]["items"]))
        await msg.channel.send(c)

@log(command="taprice")
@bot.command(name="tabyfor", aliases=["塔购买"])
async def ta_price(msg: Message, item_name: str = ""):
    if not item_name:
        raise Exception("输入格式有误。\n正确格式为: /taprice {编号} 或 /塔价格 {编号}")
    else:
        data = await fetch_item_price_by_name(item_name)
        c = CardMessage(*CS.taItemPriceCard(data["data"]["items"]))
        await msg.channel.send(c)

@log(command="hideout_all")
@bot.command(name="hideout_all", aliases=["藏身处满级"])
async def ta_price(msg: Message, version: str = ""):
    if not version:
        await msg.channel.send(("当前未输入版本，默认为黑边(仓库满级不做计算) 如果需要修改 /藏身处满级 白边"))
    data = await fetch_hideout_all()
    # c = CardMessage(*CS.hideoutStationsCard(data["data"]["hideoutStations"], version == "黑边" or version == ""))
    item_req = {}
    for ca in data["data"]["hideoutStations"]:
        if (version == "黑边" or version == "") and ca["name"] == "仓库":
            continue
        for l in ca["levels"]:
            for i in l["itemRequirements"]:
                if i["item"]["name"] in item_req:
                    item_req[i["item"]["name"]] += i["count"]
                else:
                    item_req[i["item"]["name"]] = i["count"]
    with open("hideout_find.json", "r") as f:
        d = json.load(f)
        if msg.author.id in d:
            for name in d[str(msg.author.id)].keys():
                if name in item_req.keys():
                    item_req[name] -= d[str(msg.author.id)][name]
    await msg.channel.send(json.dumps(item_req, indent=2, ensure_ascii=False))


@log(command="hideout_find")
@bot.command(name="hideout_find", aliases=["藏身处找到"])
async def ta_price(msg: Message, item_name: str = "", number: str = ""):
    if not item_name:
        await msg.channel.send("当前未输入物品名称，正确格式 /藏身处找到 {name} {number}")
        return
    if not number:
        await msg.channel.send("当前未输入数量，正确格式 /藏身处找到 {name} {number}")
        return
    with open("hideout_find.json", "r") as f:
        d = json.load(f)
        if str(msg.author.id) in d:
            if item_name in d[str(msg.author.id)]:
                d[str(msg.author.id)][item_name] += int(number)
            else:
                d[str(msg.author.id)][item_name] = int(number)
        else:
            d[str(msg.author.id)] = {item_name: int(number)}
    with open("hideout_find.json", "w+") as f:
        json.dump(d, f, indent=2, ensure_ascii=False)
    await msg.channel.send(f"在之后统计时，会减少 {item_name} 需求数 {d[str(msg.author.id)][item_name]} 个")


############### 塔科夫结束 #################
@log(command="debug")
@bot.command(name="debug")
async def debug(msg: Message):
    if msg.author.id in settings.admin_users:
        settings.debug = not settings.debug
        if settings.debug:
            await msg.channel.send("debug switch is on")
        else:
            await msg.channel.send("debug switch is off")
    else:
        await msg.channel.send("permission denied")

@log(command="warn")
@bot.command(name="warn")
async def operate_warned_user_list(msg: Message, action: str = "", user_id: str = ""):
    if msg.author.id in settings.admin_users:
        if action not in ["add", "remove", "list", "rm", "ls"]:
            raise Exception(f"unknown action: {action}")
        if not user_id and action not in ["list", "ls"]:
            raise Exception("missing user id")
        if action in ["add"]:
            settings.warned_user_list.append(user_id)
            await msg.channel.send(f"user: {user_id} has been added to warned user list")
        if action in ["remove", "rm"]:
            if user_id not in settings.warned_user_list:
                raise Exception(f"user: {user_id} is not in warned user list")
            else:
                settings.warned_user_list.remove(user_id)
                await msg.channel.send(f"user {user_id} has been removed from warned user list")
        if action in ["list", "ls"]:
            await msg.channel.send(f"current warned user list is {settings.warned_user_list}")

    else:
        await msg.channel.send("permission denied")


@bot.command(name="ban")
@log(command="ban")
async def operate_banned_user_list(msg: Message, action: str = "", user_id: str = ""):
    if msg.author.id in settings.admin_users:
        if action not in ["add", "remove", "list", "rm", "ls"]:
            raise Exception(f"unknown action: {action}")
        if not user_id and action not in ["list", "ls"]:
            raise Exception("missing user id")
        if action in ["add"]:
            settings.banned_user_list.append(user_id)
            await msg.channel.send(f"user: {user_id} has been added to banned user list")
        if action in ["remove", "rm"]:
            if user_id not in settings.banned_user_list:
                raise Exception(f"user: {user_id} is not in banned user list")
            else:
                settings.banned_user_list.remove(user_id)
                await msg.channel.send(f"user {user_id} has been removed from banned user list")
        if action in ["list", "ls"]:
            await msg.channel.send(f"current banned user list is {settings.banned_user_list}")

    else:
        await msg.channel.send("permission denied")


@bot.command(name="logout")
@log(command="logout")
async def logout(msg: Message):
    if msg.author.id in settings.admin_users:
        await msg.channel.send("logging out now...")
        raise KeyboardInterrupt()
    else:
        await msg.channel.send("permission denied")


@bot.task.add_interval(seconds=60)
async def check_ip_change():
    global previous_ip
    while True:
        if current_ip:
            if current_ip != previous_ip:
                current_ip = get_public_ip()
                channels = channel_bind.get_data()
                for server_id in channels:
                    channel_id = channels[server_id]
                    ip_change_cheannel = await bot.client.fetch_public_channel(channel_id)
                await ip_change_cheannel.send(f"你的IP地址已经变更为:{current_ip}, 所有服务暂停10~20分钟，请耐心等待,如果有服务超过1小时仍无法使用,联系血糯米")
                # 执行你想要执行的命令
                # 这里可以是调用其他函数、运行其他脚本等等
                # 示例：os.system("your_command")
                # 示例：subprocess.run(["your_command", "arg1", "arg2"])
                previous_ip = current_ip
            else:
                print("IP地址未变更")
        else:
            print("Unable to retrieve public IP address.")

# startup events
@bot.task.add_date()
async def startup_tasks():
    global previous_ip
    previous_ip = get_public_ip()

@bot.task.add_interval(minutes=3)
async def three_minutes_interval_tasks():
    await update_kanban_info(bot=bot)
    # await update_playing_game_status(bot=bot)


@bot.task.add_interval(minutes=20)
async def twenty_minutes_interval_tasks():
    await keep_bot_market_heart_beat()


# buttons reflection event, WIP
from khl import Event, EventTypes
import datetime

@bot.on_event(EventTypes.JOINED_CHANNEL)
async def user_joined_voice_channel(b: Bot, event: Event):
    channel = await b.client.fetch_public_channel(event.body['channel_id'])
    user = await b.client.fetch_user(event.body['user_id'])
    # if user.id in settings.admin_users:
    #     return
    guild = await b.client.fetch_guild(channel.guild_id)
    if guild.open_id not in channel_bind.get_data():
        return
    history_channel_id = channel_bind.get_data()[guild.open_id]
    history_channel = await b.client.fetch_public_channel(history_channel_id)
    cu_time = datetime.datetime.fromtimestamp(int(event.body['joined_at']) / 1000)
    await history_channel.send(CardMessage(CS.channel_card(user.nickname, channel.name, cu_time, "加入")))


@bot.on_event(EventTypes.EXITED_CHANNEL)
async def user_joined_voice_channel(b: Bot, event: Event):
    channel = await b.client.fetch_public_channel(event.body['channel_id'])
    user = await b.client.fetch_user(event.body['user_id'])
    # if user.id in settings.admin_users:
    #     return
    guild = await b.client.fetch_guild(channel.guild_id)
    if guild.open_id not in channel_bind.get_data():
        return
    history_channel_id = channel_bind.get_data()[guild.open_id]
    history_channel = await b.client.fetch_public_channel(history_channel_id)
    cu_time = datetime.datetime.fromtimestamp(int(event.body['exited_at']) / 1000)
    await history_channel.send(CardMessage(CS.channel_card(user.nickname, channel.name, cu_time, "离开")))

##################


async def update_cardmessage(message: Message, content: CardMessage):
    try:
        content_str = json.dumps(content)
        await update_cardmessage_by_bot(bot, message.id, content_str)
    except:
        await message.delete()
        await message.ctx.channel.send(content)

###################
# I personally think the following features (personalized regular matching commands, contributed by Froyo) 
# are suitable for a private bot, not for an open source release, I've commented this part out for now, 
# if I have better thoughts and ideas I'll restore these features.
#                                                                        -- manako. 11th, June, 2022.
###################
