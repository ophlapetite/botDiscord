import os
import discord
from discord.ext import commands

intents = discord.Intents.all()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents = intents)
client = discord.Client(intents = discord.Intents.all())


#@bot.command()
#async def bonjour(ctx):
#  await ctx.send(f"Bonjour {ctx.author}!")

#@bot.event
#async def on_message(message):
#  if not message.author.bot:
#    await message.channel.send("Bonjour c'est le bot!")


# Événement on_member_join
@bot.event
async def on_member_join(member):
    
      welcome_channel = discord.utils.get(member.guild.text_channels, name="bienvenue-et-règles")
      if welcome_channel is not None:
        await welcome_channel.send(f"Bienvenue sur le serveur de NSI {member.mention}, n'oublie pas de te renommer! 🔫")

  
token = os.environ['TOKEN_BOT_DISCORD']
bot.run(token)