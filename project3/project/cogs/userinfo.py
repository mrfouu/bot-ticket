import discord
from discord.ext import commands

class UserInfoCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def userinfo(self, ctx, member: discord.Member = None):
        """Affiche des informations détaillées sur un utilisateur."""
        member = member or ctx.author

        embed = discord.Embed(
            title=f"Informations sur {member}",
            color=discord.Color.blue()
        )
        embed.set_thumbnail(url=member.display_avatar.url)

        embed.add_field(name="Nom d'utilisateur", value=member.name, inline=True)
        embed.add_field(name="Tag", value=member.discriminator, inline=True)
        embed.add_field(name="ID", value=member.id, inline=False)
        embed.add_field(name="Date de création du compte", value=member.created_at.strftime("%d/%m/%Y à %H:%M:%S"), inline=True)
        embed.add_field(name="Date d'entrée dans le serveur", value=member.joined_at.strftime("%d/%m/%Y à %H:%M:%S") if member.joined_at else "Non disponible", inline=True)

        roles = ", ".join([role.mention for role in member.roles if role.name != "@everyone"])
        embed.add_field(name="Rôles", value=roles if roles else "Aucun rôle", inline=False)

        embed.set_footer(text=f"Demandé par {ctx.author}", icon_url=ctx.author.display_avatar.url)

        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(UserInfoCog(bot))
