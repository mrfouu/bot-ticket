import discord
from discord.ext import commands
import os
import asyncio
import json
import os

config_path = os.path.join(os.path.dirname(__file__), "config.json")
with open(config_path, "r") as file:
    config = json.load(file)

# Charger les intents nécessaires pour le bot
intents = discord.Intents.default()
intents.messages = True  # Autorise le bot à lire les messages envoyés dans les salons
intents.message_content = True  # Permet de lire le contenu des messages (nécessaire pour les commandes textuelles)
intents.guilds = True  # Permet d'interagir avec les serveurs
intents.members = True  # Permet de gérer les membres (utile pour la gestion des salons et des tickets)
intents.reactions = True  # Permet d'ajouter ou de gérer les réactions
# Chargement de la configuration

bot = commands.Bot(command_prefix=config["prefix"], intents=discord.Intents.all())


@bot.event
async def on_ready():
    print(f"Connecté en tant que {bot.user}")
    activity = discord.Activity(type=discord.ActivityType.listening, name="PNL")
    await bot.change_presence(status=discord.Status.online, activity=activity)


# Fonction pour charger les cogs
async def load_extensions():
    cogs_path = os.path.join(os.path.dirname(__file__), "cogs")
    if not os.path.exists(cogs_path):
        print(f"Le dossier 'cogs' est introuvable : {cogs_path}")
        return

    for filename in os.listdir(cogs_path):
        if filename.endswith(".py"):
            try:
                await bot.load_extension(f"cogs.{filename[:-3]}")
                print(f"Extension chargée : cogs.{filename[:-3]}")
            except Exception as e:
                print(f"Erreur lors du chargement de l'extension {filename}: {e}")

# lister les cogs sur le serveur
@bot.command()
async def loaded_cogs(ctx):
    """Affiche la liste des cogs chargés."""
    cogs = list(bot.cogs.keys())
    if cogs:
        await ctx.send(f"Cogs actuellement chargés : {', '.join(cogs)}")
    else:
        await ctx.send("Aucun cog n'est actuellement chargé.")



# Commande ping pour tester si le bot fonctionne
@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")


# Lancement du bot
async def main():
    await load_extensions()
    await bot.start(config["token"])



if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
