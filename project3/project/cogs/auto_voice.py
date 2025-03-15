import discord
from discord.ext import commands

class ChannelAndVoiceManager(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.hub_channel_ids = [1350446653295038484, 1344763125437698138, 1343612516965552158]  # IDs des hubs vocaux
        self.temp_channels = {}  # Dictionnaire pour suivre les salons temporaires {channel_id: user_id}
        self.user_temp_channel_limit = {}  # Dictionnaire pour limiter les salons temporaires par utilisateur

    @commands.command(name="createchannel")
    async def create_channel(self, ctx, channel_name: str):
        """Créer un nouveau salon texte uniquement pour les utilisateurs avec le rôle Premium."""
        guild = ctx.guild
        member = ctx.author
        
        # Vérifie si l'utilisateur a le rôle Premium
        premium_role = discord.utils.get(guild.roles, name="Premium ⭐️")
        if premium_role not in member.roles:
            await ctx.send("Vous devez posséder le rôle Premium pour créer un salon texte.")
            return

        existing_channel = discord.utils.get(guild.channels, name=channel_name)
        if existing_channel:
            await ctx.send(f"Un salon avec le nom `{channel_name}` existe déjà.")
        else:
            await guild.create_text_channel(channel_name)
            await ctx.send(f"Le salon `{channel_name}` a été créé.")

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        guild = member.guild

        # Vérifie si l'utilisateur possède le rôle Premium
        premium_role = discord.utils.get(guild.roles, name="Premium ⭐️")

        # Cas 1 : L'utilisateur rejoint un salon "Hub Vocal"
        if after.channel and after.channel.id in self.hub_channel_ids:
            # Si l'utilisateur n'a pas le rôle Premium et a déjà un salon temporaire, on empêche la création
            if premium_role not in member.roles:
                if member.id in self.user_temp_channel_limit:
                    await member.move_to(None)  # Expulse l'utilisateur du hub vocal
                    await member.send("Vous ne pouvez créer qu'un seul salon vocal temporaire sans le rôle Premium.")
                    return

            # Création d'un salon vocal temporaire
            temp_channel = await guild.create_voice_channel(
                name=f"Salon de {member.display_name}",
                category=after.channel.category  # Place dans la même catégorie que le "Hub Vocal"
            )

            # Déplace l'utilisateur dans le nouveau salon
            await member.move_to(temp_channel)

            # Enregistre le salon temporaire et limite l'utilisateur
            self.temp_channels[temp_channel.id] = member.id
            self.user_temp_channel_limit[member.id] = temp_channel.id

        # Cas 2 : Vérifie si un salon temporaire devient vide
        if before.channel and before.channel.id in self.temp_channels:
            temp_channel = before.channel

            # Si le salon est vide, on le supprime
            if len(temp_channel.members) == 0:
                await temp_channel.delete()
                del self.temp_channels[temp_channel.id]

                # Supprime la limite pour l'utilisateur
                user_id = self.temp_channels.get(temp_channel.id)
                if user_id and user_id in self.user_temp_channel_limit:
                    del self.user_temp_channel_limit[user_id]

async def setup(bot):
    await bot.add_cog(ChannelAndVoiceManager(bot))
