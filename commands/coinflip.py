from discord.ext import commands
import random

@commands.command(
    aliases = ['cf'],
    help = "Flip a coin to determine heads or tails!",
    description = "**Coinflip**",
    brief = "Flip a coin!"
)
async def coinflip(ctx):
    num = random.randint(1, 100)

    if num < 49:
        await ctx.reply("heads")
    elif num >= 50:
        await ctx.reply("tails")
    else:
        await ctx.reply("something went wrong..")
    
async def setup(bot):
    bot.add_command(coinflip)