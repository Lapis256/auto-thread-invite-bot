from discord import Intents, AllowedMentions
from discord.ext import commands


async def _get_prefix(bot, message):
    prefix = (".", )
    return commands.when_mentioned_or(*prefix)(bot, message)


def _get_intents():
    intents = Intents.all()
    intents.bans = False
    intents.typing = False
    intents.invites = False
    intents.dm_messages = False
    intents.dm_reactions = False
    intents.typing = False
    intents.presences = False
    
    return intents

import asyncio

import sys
from importlib import reload

from discord.ext.commands.bot import _is_submodule

class Bot(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(
            command_prefix=_get_prefix,
            intents=_get_intents(),
            allowed_mentions=AllowedMentions.none(),
            case_insensitive=True,
            *args, **kwargs
        )

    async def on_ready(self):
        print("ready")

    def full_reload_extension(self, name, *, package=None):
        self.reload_extension(name, package=package)

        extension_name = self._resolve_name(name, package)
        for module_name, module in sys.modules.items():
            if _is_submodule(extension_name, module_name):
                reload(module)
