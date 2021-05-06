import discord
from discord.ext import commands

import load_json_variable as variable
import crawling as cr
import crawling_qtum as crq
import crawling_doge as crd

prefix = "!"
bot = commands.Bot(command_prefix=prefix)

@bot.event
async def on_ready():
    game = discord.Game("최병덕의 전자회로")
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

@bot.command(name="qtum")
async def react_ada(ctx):
    await ctx.channel.send(crq.get_qtum_usdt())
    return None

@bot.command(name="doge")
async def react_doge(ctx):
    await ctx.channel.send(crd.get_doge_usdt())
    return None

bot.run(variable.get_token())
