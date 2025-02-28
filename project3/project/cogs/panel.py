from discord.ext import commands
import discord

class Panel(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="panel")
    async def panel_command(self, ctx):
        """Créer un panneau d'interactions."""
        embed = discord.Embed(title="Panneau", description="Cliquez sur un bouton pour interagir.", color=0x00ff00)
        view = discord.ui.View()

        # Ajout d'un bouton
        view.add_item(discord.ui.Button(label="Créer un ticket", style=discord.ButtonStyle.green, custom_id="create_ticket"))

        await ctx.send(embed=embed, view=view)

async def setup(bot):
    await bot.add_cog(Panel(bot))
