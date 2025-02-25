import discord
from discord.ext import commands

# Initialise le bot
intents = discord.Intents.default()
intents.guilds = True
intents.voice_states = True
intents.members = True
intents.messages = True
bot = commands.Bot(command_prefix="!", intents=intents)

# Dictionnaire pour suivre les salons temporaires
temporary_channels = {}

# ID du salon vocal principal (remplace par l'ID de ton salon)
MAIN_VOICE_CHANNEL_ID = 944957502473269378
MAIN_VOICE_CHANNEL_ID = 1343992632988270773

# ID du salon texte pour les messages de bienvenue et d'aurevoir (remplace par l'ID de ton salon texte)
WELCOME_CHANNEL_ID = 1261826772291420170

@bot.event
async def on_ready():
    print(f"Connecté en tant que {bot.user}")

@bot.event
async def on_voice_state_update(member, before, after):
    guild = member.guild

    # Si un utilisateur rejoint le salon principal
    if after.channel and after.channel.id == MAIN_VOICE_CHANNEL_ID:
        # Créer un salon vocal temporaire
        category = after.channel.category
        temp_channel = await guild.create_voice_channel(
            name=f"Salon de {member.display_name}",
            category=category
        )

        # Déplacer l'utilisateur dans le salon temporaire
        await member.move_to(temp_channel)

        # Enregistrer le salon temporaire
        temporary_channels[temp_channel.id] = temp_channel

    # Si un utilisateur quitte un salon temporaire
    if before.channel and before.channel.id in temporary_channels:
        temp_channel = temporary_channels[before.channel.id]

        # Vérifier si le salon est vide
        if len(temp_channel.members) == 0:
            # Supprimer le salon temporaire
            await temp_channel.delete()
            del temporary_channels[temp_channel.id]

# Gestion des messages de bienvenue et d’aurevoir
def log_member_activity():
    @bot.event
    async def on_member_join(member):
        channel = member.guild.get_channel(WELCOME_CHANNEL_ID)
        if channel:
            await channel.send(f"Bienvenue à {member.mention} qui a rejoint le serveur !")
        print(f"Bienvenue à {member.display_name} !")

    @bot.event
    async def on_member_remove(member):
        channel = member.guild.get_channel(WELCOME_CHANNEL_ID)
        if channel:
            await channel.send(f"Aurevoir à {member.display_name} qui a quitté le serveur !")
        print(f"Aurevoir à {member.display_name} !")

log_member_activity()

# Remplace 'YOUR_BOT_TOKEN' par le token de ton bot
try:
    bot.run('bot')
except ModuleNotFoundError as e:
    print("Erreur : Module non trouvé. Assurez-vous que discord.py est installé. Utilisez la commande : 'pip install discord.py'")
