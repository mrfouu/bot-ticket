import discord
from discord.ext import commands
from discord import app_commands

class HelpCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Commande slash pour /help
    @app_commands.command(name="help", description="Affiche le panel d'aide personnalisé")
    async def help(self, interaction: discord.Interaction):
        embed = discord.Embed(
            title="📘 Panel d'aide",
            description="Voici la liste des commandes disponibles, organisées par catégories :",
            color=discord.Color.blue()
        )

        # Catégorie : Publicité
        embed.add_field(
            name="🎉 Publicité",
            value="`/Sinistros` - Envoie une publicité pour un serveur Discord.",
            inline=False
        )

        # Catégorie : Gestion des salons et vocaux
        embed.add_field(
            name="🎙️ Gestion des salons et vocaux",
            value=(
                "`/createchannel [nom]` - Crée un salon texte (réservé aux membres Premium).\n"
                "`/join` - Rejoindre un hub vocal pour créer un salon temporaire."
            ),
            inline=False
        )

        # Catégorie : Rôles automatiques
        embed.add_field(
            name="🎭 Rôles automatiques",
            value=(
                "`/setup_roles` - Configure un message pour attribuer des rôles automatiquement.\n"
                "(Réagissez avec 🔥 pour obtenir le rôle Homme ou ☀ pour le rôle Femme)."
            ),
            inline=False
        )

        # Catégorie : Modération
        embed.add_field(
            name="🔧 Modération",
            value="`/clear [nombre]` - Supprime un nombre spécifié de messages (max 200).",
            inline=False
        )

        # Catégorie : Fun
        embed.add_field(
            name="🎮 Fun",
            value="`/illuzion` - Répond qu'Illuzion est le pire joueur de COD.",
            inline=False
        )

        # Catégorie : Tickets
        embed.add_field(
            name="🎟️ Tickets",
            value=(
                "`/ticketpanel` - Affiche un panneau pour créer des tickets.\n"
                "`/ticket [catégorie]` - Crée un ticket pour une catégorie spécifique."
            ),
            inline=False
        )

        # Catégorie : Informations utilisateur
        embed.add_field(
            name="👤 Informations utilisateur",
            value="`/userinfo [membre]` - Affiche des informations détaillées sur un utilisateur.",
            inline=False
        )

        # Pied de page
        embed.set_footer(text="Besoin d'aide supplémentaire ? Contactez un administrateur.")

        # Envoyer l'embed
        await interaction.response.send_message(embed=embed)

# Fonction pour ajouter le cog au bot
async def setup(bot):
    await bot.add_cog(HelpCog(bot))