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
intents.messages = True
intents.message_content = True
intents.guilds = True
intents.members = True
intents.reactions = True  # Nécessaire pour détecter les réactions
intents.guild_messages = True  # Nécessaire pour détecter les messages dans les serveurs
# Chargement de la configuration

bot = commands.Bot(command_prefix=config["prefix"], intents=discord.Intents.all(), help_command=None)


@bot.event
async def on_ready():
    print(f"Connecté en tant que {bot.user}")
    activity = discord.Activity(type=discord.ActivityType.listening, name="PNL")
    await bot.change_presence(status=discord.Status.online, activity=activity)
    try:
        synced = await bot.tree.sync()
        print(f"Commandes slash synchronisées : {len(synced)}")
    except Exception as e:
        print(f"Erreur lors de la synchronisation des commandes slash : {e}")

        

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


# Lancement du bot
async def main():
    await load_extensions()
    await bot.start(config["token"])



if __name__ == "__main__":
    import asyncio

    asyncio.run(main())