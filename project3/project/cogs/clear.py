import discord
from discord.ext import commands

class ClearCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="clear")
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount: int):
        """Supprime un certain nombre de messages (maximum 200)."""
        if amount > 200:
            await ctx.send("Vous ne pouvez pas supprimer plus de 200 messages à la fois.")
            return

        deleted = await ctx.channel.purge(limit=amount)
        await ctx.send(f"{len(deleted)} messages ont été supprimés.", delete_after=5)

async def setup(bot):
    await bot.add_cog(ClearCommand(bot))
