import discord
from discord.ext import commands

class AutoRoleCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.role_message_id = None
        self.emoji_to_role = {
            "🔥": "homme",
            "☀": "femme"
        }

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def setup_roles(self, ctx):
        embed = discord.Embed(
            title="Choisissez vos Rôles 🎭",
            description=(
                "Bienvenue ! Sélectionnez les rôles que vous souhaitez en cliquant sur les emojis correspondants ci-dessous.\n\n"
                + "\n".join([f"{emoji} **: {role}**" for emoji, role in self.emoji_to_role.items()])
            ),
            color=discord.Color.dark_teal()
        )

        if self.bot.user.avatar:
            embed.set_thumbnail(url=self.bot.user.avatar.url)
        if ctx.guild.icon:
            embed.set_author(name=ctx.guild.name, icon_url=ctx.guild.icon.url)
        embed.set_footer(text="Ajoutez ou retirez une réaction pour modifier vos rôles.")

        message = await ctx.send(embed=embed)

        for emoji in self.emoji_to_role.keys():
            await message.add_reaction(emoji)

        self.role_message_id = message.id
        await ctx.send("Message des rôles configuré avec succès !")

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        if self.role_message_id is None:
            return

        if payload.message_id != self.role_message_id:
            return

        guild = self.bot.get_guild(payload.guild_id)
        if guild is None:
            return

        member = guild.get_member(payload.user_id)
        if member is None:
            return

        emoji = str(payload.emoji)
        if emoji in self.emoji_to_role:
            role_name = self.emoji_to_role[emoji]
            role = discord.utils.get(guild.roles, name=role_name)

            if role and role not in member.roles:
                await member.add_roles(role)

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):
        if self.role_message_id is None:
            return

        if payload.message_id != self.role_message_id:
            return

        guild = self.bot.get_guild(payload.guild_id)
        if guild is None:
            return

        member = guild.get_member(payload.user_id)
        if member is None:
            return

        emoji = str(payload.emoji)
        if emoji in self.emoji_to_role:
            role_name = self.emoji_to_role[emoji]
            role = discord.utils.get(guild.roles, name=role_name)

            if role and role in member.roles:
                await member.remove_roles(role)

async def setup(bot):
    await bot.add_cog(AutoRoleCog(bot))
