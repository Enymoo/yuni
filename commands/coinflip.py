from discord.ext import commands
import random

@commands.command(
    aliases = ['cf'],
    help = "Flip a coin to determine heads or tails!",
    description = "**Coinflip**",
    brief = "Flip a coin!"
)
async def coinflip(ctx):
    result = random.choice(["Tails", "Heads", "Heads", "Tails"])
    await ctx.send(result)

async def setup(bot):
    bot.add_command(coinflip)