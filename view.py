from discord import (
    ButtonStyle,
    Embed
)
from discord.ext.ui import (
    Component,
    Button,
    View,
    Message
)


class RolePanelView(View):
    def __init__(self, bot, role):
        super().__init__(bot)
        self.bot = bot
        self.role = role

    async def click(self, interaction):
        guild = interaction.guild

        member = interaction.user
        if self.role in member.roles:
           await member.remove_roles(self.role)
           await interaction.response.send_message(
               "解除しました。",
                ephemeral=True
            )
        else:
           await member.add_roles(self.role)
           await interaction.response.send_message(
                "設定しました。",
                ephemeral=True
            )

    async def body(self):
        return Message(
            embed=Embed(
                title="スレッド自動参加設定",
                description=("ボタンを押すとスレッドの作成時に"
                "メンションされ、自動で参加できるようなります。\n"
                "解除するにはもう一度ボタンを押してください。")
            ),
            component=Component(items=[
                [
                    Button("設定")
                        .emoji("\N{BELL}")
                        .style(ButtonStyle.blurple)
                        .on_click(self.click)
                        .custom_id(f"role_button:{self.role.id}")
                ]
            ])
        )
