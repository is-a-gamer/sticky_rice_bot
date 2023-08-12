import json
from app.tarkov.query_build import GQueryBuilder, base_item_query
import aiohttp

TARKOV_API_BASE_URL = "https://api.tarkov.dev"
TARKOV_API_GRAPHQL_URL = f"{TARKOV_API_BASE_URL}/graphql"

async def fetch_item_data_by_name(name):
    url = TARKOV_API_GRAPHQL_URL
    query = base_item_query({"name": name})
    async with aiohttp.ClientSession(headers={"Content-Type": "application/json"}) as session:
        async with session.post(url, data=query) as r:
            resp_json = await r.json()
            return resp_json

# async def fetch_item_data_by_name(name: str):
#     url = f"{TARKOV_API_BASE_URL}?/graphql"
#     async with aiohttp.ClientSession() as session:
#         async with session.post(url,data=) as r:
#             resp_json = await r.json()
#             status = resp_json.get("code", 1)
#             if status != 0:
#                 raise Exception(resp_json.get("message", "fetch video info failed, unknown reason."))
#             else:
#                 data = resp_json.get("data", {})
#                 if data:
#                     matched = True
#                     name = data.get("title", "未知视频")
#                     author = data.get("owner", {}).get("name", "未知up主")
#                     cid = data.get("cid", 0)
#                     duration = data.get("duration", 180)  # seconds
#                     duration *= 1000
#                     cover_image_url = data.get("pic", "")
#                 else:
#                     matched = False
#                     name = ""
#                     author = ""
#                     cid = 0
#                     duration = 0
#                     cover_image_url = ""
#     logger.debug(f"{[matched, name, author, cid, duration, cover_image_url]}")
#     return matched, name, author, cid, duration, cover_image_url
