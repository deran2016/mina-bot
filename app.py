import discord
from discord.ext import commands

import load_json_variable as variable
import crawling as cr

prefix = "!"
bot = commands.Bot(command_prefix=prefix)

@bot.event
async def on_ready():
    game = discord.Game("논리회로설계실험")
    await bot.change_presence(status=discord.Status.online, activity=game)
    print("READY")

@bot.event
async def on_message(message):
    if message.author.bot:
        return None

    await bot.process_commands(message)

@bot.command(name="mina")
async def react_mina(ctx):
    await ctx.channel.send(cr.get_mina_usdt())
    return None

bot.run(variable.get_token())
