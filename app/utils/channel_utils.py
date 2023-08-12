from khl import Bot, Message


async def get_joined_voice_channel_id(bot: Bot, guild_id: str, user_id: str) -> str: 
    method = "GET"
    route = "channel-user/get-joined-channel"
    resp_data = await bot.client.gate.request(method=method, route=f"{route}?guild_id={guild_id}&user_id={user_id}")
    items = resp_data.get("items", [])
    if items:
        channel_id = items[0].get("id", "")
    else:
        channel_id = ""
    return channel_id

async def update_channel_name_by_message(msg: Message, channel_id: str, new_name: str):
    method = "POST"
    route = "channel/update"
    json = {
        "channel_id": channel_id,
        "name": new_name,
    }
    await msg.ctx.gate.request(method=method, route=route, json=json)    

async def update_channel_name_by_bot(bot: Bot, channel_id: str, new_name: str):
    method = "POST"
    route = "channel/update"
    json = {
        "channel_id": channel_id,
        "name": new_name,
    }
    await bot.client.gate.request(method=method, route=route, json=json)

async def get_channel_user_by_channel_id(bot: Bot, channel_id: str, new_name: str):
    method = "GET"
    route = "channel/user-list"
    json = {
        "channel_id": channel_id,
    }
    await bot.client.gate.request(method=method, route=route, json=json)
