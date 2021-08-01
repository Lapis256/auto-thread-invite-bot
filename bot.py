from discord import (
    Client,
    AllowedMentions,
    Intents,
    MemberCacheFlags,
    InteractionType
)

from view import RolePanelView
from db import add, get_all, get_all_from_guild_id


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
        self.view_added = False

    async def on_interaction(self, interaction):
        if interaction.type != InteractionType.application_command:
            return

        data = interaction.data
        if data["name"] != "create_setting_panel":
            return

        guild = interaction.guild
        if guild is None:
            return

        role_id = int(data["options"][0]["value"])
        role = guild.get_role(role_id)

        if not interaction.user.guild_permissions.administrator:
            await interaction.response.send_message(
                "このコマンドは管理者権限がないと使用できません。",
                ephemeral=True
            )
            return

        if guild.me.top_role < role:
            await interaction.response.send_message(
                ("指定されたロールは使用できません。\n"
                "Botが持つ最高権限のロールより下に配置してください。"),
                ephemeral=True
            )
            return

        if not role.mentionable:
            await interaction.response.send_message(
                "メンション可能なロールを指定してください。",
                ephemeral=True
            )
            return

        await interaction.response.send_message("Success")
        await interaction.delete_original_message()
     
        view = await RolePanelView(self, role).setup()
        await interaction.channel.send(**view.build())

        await add(role_id, interaction.guild_id)

    async def on_ready(self):
        print("ready")

        if self.view_added:
            return

        for _role in await get_all():
            guild = self.get_guild(_role.guild_id)
            role = guild.get_role(_role.id)
            if role is None:
                await _role.delete()
                continue

            view = await RolePanelView(self, role).setup()
            self.add_view(view)

        self.view_added = True

    async def on_thread_join(self, thread):
        if thread.me is not None:
            return

        guild = thread.guild
        roles = await get_all_from_guild_id(guild.id)
        mentions = []
        for _role in roles:
            role = guild.get_role(_role.id)
            if role is None:
                await _role.delete()
                continue
            mentions.append(role.mention)

        message = await thread.send(", ".join(mentions))
        await message.delete()
