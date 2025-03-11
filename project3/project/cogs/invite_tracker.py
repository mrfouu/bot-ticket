import discord
from discord.ext import commands

class InviteTracker(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.invites = {}  # Stocke les invitations pour chaque serveur

    @commands.Cog.listener()
    async def on_ready(self):
        """Initialise les invitations pour tous les serveurs."""
        for guild in self.bot.guilds:
            self.invites[guild.id] = await guild.invites()
        print("Les invitations ont été chargées.")

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        """Charge les invitations lorsqu'un bot rejoint un nouveau serveur."""
        self.invites[guild.id] = await guild.invites()

    @commands.Cog.listener()
    async def on_member_join(self, member):
        """Détecte qui a invité un membre."""
        guild = member.guild

        # Récupérer les invitations actuelles
        new_invites = await guild.invites()
        old_invites = self.invites.get(guild.id, [])

        # Identifier l'invitation utilisée
        used_invite = None
        for invite in new_invites:
            for old_invite in old_invites:
                if invite.code == old_invite.code and invite.uses > old_invite.uses:
                    used_invite = invite
                    break

        # Mettre à jour les invitations pour le serveur
        self.invites[guild.id] = new_invites

        # Envoyer un message dans un salon désigné si l'invitation est trouvée
        if used_invite:
            inviter = used_invite.inviter
            channel = discord.utils.get(guild.text_channels, name="logs")  # Nom du salon de logs
            if channel:
                await channel.send(f"{member.mention} a rejoint le serveur grâce à l'invitation de {inviter.mention}. ({used_invite.uses} utilisations)")
        else:
            print(f"Impossible de déterminer l'invitation utilisée pour {member.name}.")

async def setup(bot):
    await bot.add_cog(InviteTracker(bot))
