from discord.ext import commands

class Illuzion(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="illuzion")
    async def illuzion_command(self, ctx):
        """Répond que Illuzion est le pire joueur de COD."""
        await ctx.send("Illuzion est le pire joueur de COD ! 😜")

async def setup(bot):
    await bot.add_cog(Illuzion(bot))
