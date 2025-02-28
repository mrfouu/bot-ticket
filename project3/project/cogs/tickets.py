import discord
from discord.ext import commands
from discord.ui import View, Button

class Tickets(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def create_ticket(self, interaction: discord.Interaction, category_name: str):
        """Créer un ticket avec un bouton pour fermer."""
        guild = interaction.guild
        overwrites = {
            guild.default_role: discord.PermissionOverwrite(read_messages=False),
            interaction.user: discord.PermissionOverwrite(read_messages=True),
        }

        # Ajout du préfixe "ticket-" pour le salon
        ticket_channel = await guild.create_text_channel(f"ticket-{interaction.user.name}", overwrites=overwrites)
        embed = discord.Embed(
            title=f"Ticket : {category_name}",
            description="Un membre de l'équipe vous répondra bientôt. Utilisez le bouton ci-dessous pour fermer le ticket si nécessaire.",
            color=discord.Color.green(),
        )
        view = TicketButtonView(self.bot, interaction.user)
        await ticket_channel.send(embed=embed, view=view)

    @commands.Cog.listener()
    async def on_interaction(self, interaction: discord.Interaction):
        """Gestion des interactions avec les boutons."""
        try:
            print(f"Interaction détectée : {interaction.data}")  # Log des interactions

            if interaction.data["custom_id"] == "create_bot":
                await self.create_ticket(interaction, "Création de Bot")
                await interaction.response.send_message("Votre ticket a été créé.", ephemeral=True)
            elif interaction.data["custom_id"] == "premium_bot":
                await self.create_ticket(interaction, "Premium Bot")
                await interaction.response.send_message("Votre ticket a été créé.", ephemeral=True)
            elif interaction.data["custom_id"] == "support":
                await self.create_ticket(interaction, "Support Général")
                await interaction.response.send_message("Votre ticket a été créé.", ephemeral=True)
            elif interaction.data["custom_id"] == "close_ticket":
                if interaction.channel.name.startswith("ticket-"):
                    await interaction.channel.delete()
                    print(f"Salon {interaction.channel.name} supprimé.")  # Log
                else:
                    await interaction.response.send_message(
                        "Ce bouton ne peut être utilisé que dans un salon de ticket.",
                        ephemeral=True,
                    )
            else:
                await interaction.response.send_message("Action non reconnue.", ephemeral=True)

        except Exception as e:
            print(f"Erreur dans on_interaction : {e}")  # Log des erreurs


class TicketButtonView(View):
    def __init__(self, bot, user):
        super().__init__(timeout=None)
        self.bot = bot
        self.user = user

        # Ajouter uniquement le bouton pour fermer un ticket
        self.add_item(Button(label="Fermer le ticket", style=discord.ButtonStyle.danger, custom_id="close_ticket"))


async def setup(bot):
    """Ajoute le cog Tickets."""
    await bot.add_cog(Tickets(bot))
