import asyncio
import json

import aiohttp

TARKOV_API_BASE_URL = "https://api.tarkov.dev"
TARKOV_API_GRAPHQL_URL = f"{TARKOV_API_BASE_URL}/graphql"
new_query = json.dumps({"query": '''
        {
          items(name: "m855a1") {
            id
            name
            shortName
            basePrice
            link
          }
        }
'''}, indent=4)


async def fetch_item_data_by_name():
    url = TARKOV_API_GRAPHQL_URL
    async with aiohttp.ClientSession(headers={"Content-Type": "application/json"}) as session:
        async with session.post(url, data=new_query) as r:
            resp_json = await r.json()
            print(json.dumps(resp_json, indent=4))


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(fetch_item_data_by_name())
    loop.close()
