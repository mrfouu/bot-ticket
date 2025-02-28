import discord
from discord.ext import commands
from discord.ui import View, Button

class TicketPanel(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="ticketpanel")
    async def ticketpanel(self, ctx):
        """Crée un panneau de tickets avec des boutons."""
        embed = discord.Embed(
            title="🎟️ Panel de Tickets",
            description=(
                "Bienvenue dans le support !\n"
                "Veuillez sélectionner la catégorie de votre ticket :\n\n"
                "**1. Création de bot personnalisé**\n"
                "**2. Premium Bot**\n"
                "**3. Support général**\n\n"
                "Cliquez sur le bouton correspondant ci-dessous."
            ),
            color=discord.Color.blurple()
        )
        view = TicketPanelView(self.bot)
        await ctx.send(embed=embed, view=view)


class TicketPanelView(View):
    def __init__(self, bot):
        super().__init__(timeout=None)
        self.bot = bot

        # Ajouter les boutons pour chaque catégorie
        self.add_item(Button(label="Création de Bot", style=discord.ButtonStyle.primary, custom_id="create_bot"))
        self.add_item(Button(label="Premium Bot", style=discord.ButtonStyle.success, custom_id="premium_bot"))
        self.add_item(Button(label="Support Général", style=discord.ButtonStyle.secondary, custom_id="support"))

    async def interaction_check(self, interaction: discord.Interaction) -> bool:
        """Vérifie si l'interaction est valide."""
        print(f"Interaction reçue dans TicketPanelView : {interaction.data}")  # Log
        return True


async def setup(bot):
    """Ajoute le cog TicketPanel."""
    await bot.add_cog(TicketPanel(bot))
