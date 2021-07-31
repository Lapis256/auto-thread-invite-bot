from os import environ

from discord import Client, AllowedMentions, Intents, MemberCacheFlags
from discord.utils import get, find
from dotenv import load_dotenv
import uvloop


class ThreadAutoInviteBot(Client):
    def __init__(self):
        super().__init__(
            allowed_mentions=AllowedMentions(
                everyone=False,
                users=False,
                roles=True,
                replied_user=False
            ),
            intents=Intents(guilds=True),
            member_cache_flags=MemberCacheFlags.none(),
            max_messages=None,
            guild_subscriptions=False,
            chunk_guilds_at_startup=False
        )
        
    async def on_ready(self):
        print("ready")

    async def on_thread_join(self, thread):
        if thread.me is not None:
            return

        role = find(
            lambda r: r.name.lower() == "threadlistener",
            thread.guild.roles
        )
        if role is None:
            return
        await thread.send(role.mention)


def main():
    bot = ThreadAutoInviteBot()
    
    uvloop.install()
    load_dotenv()
    bot.run(environ["TOKEN"])


if __name__ == "__main__":
    main()
