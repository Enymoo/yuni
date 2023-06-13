from discord.ext import commands
import random

@commands.command(
    aliases = ['cf'],
    help = "This is help",
    description = "This is description",
    brief = "This is brief"
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