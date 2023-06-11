from dotenv import load_dotenv
from discord.ext import commands
import discord, os, pathlib, settings

logger = settings.logging.getLogger("bot")

def run_discord_bot():
    load_dotenv()
    intents = discord.Intents.default()
    intents.message_content = True
    bot = commands.Bot(command_prefix="!", intents=intents)

    @bot.event
    async def on_ready():
        activity = discord.Game(name=f"!help | by @enymu")
        await bot.change_presence(activity=activity, status=discord.Status.online)
        logger.info(f"User: {bot.user.name} (ID: {bot.user.id})")

    @bot.command(
        aliases = ['cf'],
        help = "This is help",
        description = "This is description",
        brief = "This is brief"
    )
    async def coinflip(ctx):
        """ Toss a coin """
        import random
        num = random.randint(1, 100)

        if num < 49:
            await ctx.reply("heads")
        elif num >= 50:
            await ctx.reply("tails")
        else:
            await ctx.reply("something went wrong..")

        # for filename in os.listdir('./commands'):
        #     if filename.endswith('.py'):
        #         print(filename)
        #         await bot.load_extension(f'commands.{filename[:-3]}')

    bot.run(settings.SECRET, root_logger=True)