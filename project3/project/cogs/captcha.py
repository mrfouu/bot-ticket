import discord
from discord.ext import commands

class CaptchaCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.verification_role_name = "Mec Normal"  # Nom du rôle à attribuer après vérification
        self.unverified_role_name = "Non Vérifié"  # Nom du rôle initial
        self.verification_channel_id = 1351977652960890890  # Remplacez par l'ID du canal de vérification

    @commands.Cog.listener()
    async def on_member_join(self, member):
        """Donne le rôle 'Non Vérifié' aux nouveaux membres."""
        guild = member.guild
        unverified_role = discord.utils.get(guild.roles, name=self.unverified_role_name)

        if unverified_role:
            await member.add_roles(unverified_role)
        
        # Envoie un message dans le canal de vérification
        verification_channel = self.bot.get_channel(self.verification_channel_id)
        if verification_channel:
            embed = discord.Embed(
                title="Vérification requise",
                description="Cliquez sur le bouton ci-dessous pour prouver que vous êtes humain et obtenir l'accès au serveur.",
                color=discord.Color.green()
            )
            embed.set_footer(text=f"Bienvenue {member.display_name} !")
            view = VerificationView(self.verification_role_name, unverified_role)
            await verification_channel.send(content=member.mention, embed=embed, view=view)

class VerificationView(discord.ui.View):
    def __init__(self, verification_role_name, unverified_role):
        super().__init__()
        self.verification_role_name = verification_role_name
        self.unverified_role = unverified_role

    @discord.ui.button(label="Je suis humain", style=discord.ButtonStyle.green, emoji="✅")
    async def verify(self, interaction: discord.Interaction, button: discord.ui.Button):
        """Gère la vérification du membre."""
        guild = interaction.guild
        member = interaction.user
        verified_role = discord.utils.get(guild.roles, name=self.verification_role_name)

        if verified_role:
            # Retirer le rôle 'Non Vérifié' et ajouter le rôle 'Membre'
            if self.unverified_role in member.roles:
                await member.remove_roles(self.unverified_role)
            await member.add_roles(verified_role)
            await interaction.response.send_message(
                "Vérification réussie ! Vous avez maintenant accès au serveur. 🎉",
                ephemeral=True
            )
        else:
            await interaction.response.send_message(
                "Le rôle de vérification n'a pas été trouvé. Veuillez contacter un administrateur.",
                ephemeral=True
            )

async def setup(bot):
    await bot.add_cog(CaptchaCog(bot))
