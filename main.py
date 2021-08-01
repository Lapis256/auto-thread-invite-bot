from os import environ

from dotenv import load_dotenv
import uvloop

from bot import ThreadAutoInviteBot
from db import setup_db


def main():
    uvloop.install()
    load_dotenv()

    bot = ThreadAutoInviteBot()

    bot.loop.create_task(setup_db(environ["DB"]))
    bot.run(environ["TOKEN"])


if __name__ == "__main__":
    main()
