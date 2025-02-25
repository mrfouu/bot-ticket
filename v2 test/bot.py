# bot.py
import discord
from discord.ext import commands
from voice_manager import VoiceManager
from welcome_manager import WelcomeManager
from ticket_manager import TicketManager

# Initialise le bot
intents = discord.Intents.default()
intents.guilds = True
intents.voice_states = True
intents.members = True
intents.messages = True
bot = commands.Bot(command_prefix="!", intents=intents)

# Configurations
WELCOME_CHANNEL_ID = 987654321098765432  # ID du salon de bienvenue
VERIFIED_ROLE_ID = 112233445566778899  # ID du rôle après vérification
VOICE_CHANNEL_IDS = [123456789012345678, 234567890123456789]  # IDs des salons vocaux principaux
TICKET_CATEGORY_ID = 345678901234567890  # ID de la catégorie où créer les tickets

# Initialise les gestionnaires
voice_manager = VoiceManager(bot, VOICE_CHANNEL_IDS)
welcome_manager = WelcomeManager(bot, WELCOME_CHANNEL_ID, VERIFIED_ROLE_ID)
ticket_manager = TicketManager(bot, TICKET_CATEGORY_ID)

@bot.event
async def on_ready():
    print(f"Connecté en tant que {bot.user}")

# Ajoute les événements des gestionnaires
bot.add_listener(voice_manager.on_voice_state_update, "on_voice_state_update")
bot.add_listener(welcome_manager.on_member_join, "on_member_join")
bot.add_listener(welcome_manager.on_member_remove, "on_member_remove")

# Ajoute les commandes de gestion des tickets
@bot.command()
async def ticket(ctx):
    await ticket_manager.create_ticket_panel(ctx)

# Remplace 'YOUR_BOT_TOKEN' par le token de ton bot
try:
    bot.run('troll')
except ModuleNotFoundError as e:
    print("Erreur : Module non trouvé. Assurez-vous que discord.py est installé. Utilisez la commande : 'pip install discord.py'")
