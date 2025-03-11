from discord.ext import commands

class ChannelManager(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="createchannel")
    async def create_channel(self, ctx, channel_name: str):
        """Créer un nouveau salon texte."""
        guild = ctx.guild
        existing_channel = discord.utils.get(guild.channels, name=channel_name)

        if existing_channel:
            await ctx.send(f"Un salon avec le nom `{channel_name}` existe déjà.")
        else:
            await guild.create_text_channel(channel_name)
            await ctx.send(f"Le salon `{channel_name}` a été créé.")

async def setup(bot):
    await bot.add_cog(ChannelManager(bot))
