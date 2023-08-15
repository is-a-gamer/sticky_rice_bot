import json
from app.tarkov.query_build import GQueryBuilder, item_base_query, item_price_query,hideout_stations_query
import aiohttp

TARKOV_API_BASE_URL = "https://api.tarkov.dev"
TARKOV_API_GRAPHQL_URL = f"{TARKOV_API_BASE_URL}/graphql"


async def fetch_item_data_by_name(name):
    url = TARKOV_API_GRAPHQL_URL
    query = item_base_query({"name": name})
    async with aiohttp.ClientSession(headers={"Content-Type": "application/json"}) as session:
        async with session.post(url, data=query) as r:
            resp_json = await r.json()
            return resp_json


async def fetch_item_price_by_id(id):
    url = TARKOV_API_GRAPHQL_URL
    query = item_price_query({"ids": id})
    async with aiohttp.ClientSession(headers={"Content-Type": "application/json"}) as session:
        async with session.post(url, data=query) as r:
            resp_json = await r.json()
            return resp_json


async def fetch_item_price_by_name(name: str):
    url = TARKOV_API_GRAPHQL_URL
    query = item_price_query({"name": name})
    async with aiohttp.ClientSession(headers={"Content-Type": "application/json"}) as session:
        async with session.post(url, data=query) as r:
            resp_json = await r.json()
            return resp_json


async def fetch_hideout_all():
    url = TARKOV_API_GRAPHQL_URL
    query = hideout_stations_query({})
    async with aiohttp.ClientSession(headers={"Content-Type": "application/json"}) as session:
        async with session.post(url, data=query) as r:
            resp_json = await r.json()
            return resp_json
