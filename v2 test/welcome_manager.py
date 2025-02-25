# welcome_manager.py
import discord
import random

class WelcomeManager:
    def __init__(self, bot, welcome_channel_id, verified_role_id):
        self.bot = bot
        self.welcome_channel_id = welcome_channel_id  # ID du salon de bienvenue
        self.verified_role_id = verified_role_id  # ID du rôle après vérification

    async def on_member_join(self, member):
        guild = member.guild
        channel = guild.get_channel(self.welcome_channel_id)
        if channel:
            await channel.send(f"Bienvenue à {member.mention} qui a rejoint le serveur !")

        # Envoi du captcha
        captcha_code = random.randint(1000, 9999)
        try:
            captcha_message = await member.send(
                f"Bienvenue sur le serveur {guild.name} !\n\nPour accéder à toutes les fonctionnalités, veuillez entrer ce code de vérification : **{captcha_code}**"
            )

            def check(message):
                return (
                    message.author == member
                    and message.channel == captcha_message.channel
                    and message.content.isdigit()
                    and int(message.content) == captcha_code
                )

            await self.bot.wait_for("message", check=check, timeout=300)  # 5 minutes pour répondre
            role = guild.get_role(self.verified_role_id)
            if role:
                await member.add_roles(role)
                await member.send("Merci ! Vous avez été vérifié(e) et avez maintenant accès au serveur.")
        except Exception:
            await member.send("Vous n'avez pas réussi à entrer le bon code à temps. Contactez un administrateur pour de l'aide.")

    async def on_member_remove(self, member):
        channel = member.guild.get_channel(self.welcome_channel_id)
        if channel:
            await channel.send(f"Au revoir à {member.display_name} qui a quitté le serveur !")