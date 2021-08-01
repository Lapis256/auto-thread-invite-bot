import asyncio
from os import environ

from dotenv import load_dotenv
import aiohttp


async def register(token, id, data):
    headers = { "Authorization": "Bot " + token }
    url = f"https://discord.com/api/v8/applications/{id}/guilds/525995782592266250/commands"

    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.post(url, json=data) as res:
            print(f"{data['name']} {res.status}")


async def main(token, id):
    question = {
        "name": "create_setting_panel",
        "description": "設定パネルを作成します。",
        "options": [
            {
                "name": "role",
                "description": "使用するロールです。",
                "type": 8,
                "required": True
            }
        ]
    }
    await register(token, id, question)


if __name__ == '__main__':
    load_dotenv()
    asyncio.run(main(environ["TOKEN"], environ["APPLICATION_ID"]))
