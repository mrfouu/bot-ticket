# voice_manager.py
import discord

class VoiceManager:
    def __init__(self, bot, voice_channel_ids):
        self.bot = bot
        self.voice_channel_ids = voice_channel_ids  # Liste des salons vocaux principaux
        self.temporary_channels = {}  # Dictionnaire pour suivre les salons temporaires

    async def on_voice_state_update(self, member, before, after):
        guild = member.guild

        # Gestion de l'ajout à un salon principal
        if after.channel and after.channel.id in self.voice_channel_ids:
            # Créer un salon vocal temporaire
            category = after.channel.category
            temp_channel = await guild.create_voice_channel(
                name=f"Salon de {member.display_name}",
                category=category
            )

            # Déplacer l'utilisateur dans le salon temporaire
            await member.move_to(temp_channel)

            # Enregistrer le salon temporaire
            self.temporary_channels[temp_channel.id] = temp_channel

        # Gestion de la suppression d'un salon temporaire
        if before.channel and before.channel.id in self.temporary_channels:
            temp_channel = self.temporary_channels[before.channel.id]

            # Vérifier si le salon est vide
            if len(temp_channel.members) == 0:
                # Supprimer le salon temporaire
                await temp_channel.delete()
                del self.temporary_channels[temp_channel.id]
