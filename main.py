import os
from dotenv import load_dotenv
import discord
from discord.ext import commands

# Charge les variables d'environnement depuis le fichier .env
load_dotenv()

# Récupère le token du bot
token = os.getenv('TOKEN_BOT_DISCORD')

if token is None:
    print("Le token n'a pas été trouvé dans les variables d'environnement.")
else:
    print("Token chargé avec succès !")

# Initialisation du bot
intents = discord.Intents.all()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

# Votre code de bot ici
@bot.event
async def on_member_join(member):
    welcome_channel = discord.utils.get(member.guild.text_channels, name="bienvenue-et-règles")
    if welcome_channel is not None:
        await welcome_channel.send(f"Bienvenue sur le serveur de NSI {member.mention}, n'oublie pas de te renommer! 🔫")

bot.run(token)
