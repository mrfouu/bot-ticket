import discord
from discord.ext import commands

class Advertisement(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="Sinistros")
    async def send_advertisement(self, ctx):
        """Envoie une publicité pour un serveur Discord."""
        embed = discord.Embed(
            title="🎉 Rejoignez notre serveur Tournament Sinistros !",
            description=(
                "🌟 📜 Bienvenue à Poudlard, version Call of Duty ! 🎮✨\n"
                "⚔️ Que vous soyez un Gryffondor courageux, un Serpentard stratégique, un Poufsouffle fidèle ou un Serdaigle ingénieux, préparez vos baguettes et vos manettes pour des affrontements épiques.\n\n"
                "👉 Ce qui vous attend :\n"
                "- 🎯 Tournois réguliers avec des récompenses magiques 🏆\n"
                "-🗣️ Communauté active de sorciers-gamers\n"
                "-🧙 Événements spéciaux (défis et plus)\n"
                "-🕹️ Gameplay compétitif et fun, le tout dans une ambiance immersive Harry Potter\n"
                "-🪄 Défendez les couleurs de votre maison et prouve que tu es le sorcier ultime du champ de bataille !\n"
                "-✨ Une seule règle : toujours jouer avec un peu de magie ! 🔥\n\n"
                "[**📩 Rejoignez-nous maintenant !**](https://discord.gg/CMBNjt4gRz)\n"
            ),
            color=discord.Color.blue(),
        )
        embed.set_thumbnail(url="https://i.goopics.net/3isn03.png")  # URL vers une image de présentation
        embed.set_footer(text="Nous avons hâte de vous accueillir ! 🚀")
        
        # Envoie de l'embed dans le canal actuel
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Advertisement(bot))
