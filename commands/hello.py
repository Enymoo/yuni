from discord.ext import commands

@commands.command()
async def hello(self, ctx):
    await ctx.send("hi! :3")

async def setup(bot):
    bot.add_command(hello)