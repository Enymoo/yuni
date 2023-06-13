from discord.ext import commands
import random

@commands.command(
    help = "This is help",
    description = "This is description",
    brief = "This is brief"
)
async def register(ctx):
    pass
    
async def setup(bot):
    bot.add_command(register)