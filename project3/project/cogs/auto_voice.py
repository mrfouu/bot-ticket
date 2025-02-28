import discord
from discord.ext import commands

class AutoVoice(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.hub_channel_ids = [1343621843952861224, 1344763125437698138, 1343612516965552158]  # Liste des ID des salons vocaux "Hub"
        self.temp_channels = {}  # Dictionnaire pour suivre les salons temporaires {channel_id: user_id}

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        guild = member.guild

        # Cas 1 : L'utilisateur rejoint un salon "Hub Vocal"
        if after.channel and after.channel.id in self.hub_channel_ids:
            # Création d'un salon vocal temporaire
            temp_channel = await guild.create_voice_channel(
                name=f"Salon de {member.display_name}",
                category=after.channel.category  # Place dans la même catégorie que le "Hub Vocal"
            )

            # Déplace l'utilisateur dans le nouveau salon
            await member.move_to(temp_channel)

            # Enregistre le salon temporaire
            self.temp_channels[temp_channel.id] = member.id

        # Cas 2 : Vérifie si un salon temporaire devient vide
        if before.channel and before.channel.id in self.temp_channels:
            temp_channel = before.channel

            # Si le salon est vide, on le supprime
            if len(temp_channel.members) == 0:
                await temp_channel.delete()
                del self.temp_channels[temp_channel.id]

async def setup(bot):
    await bot.add_cog(AutoVoice(bot))
