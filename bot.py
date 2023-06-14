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

        for cmd_file in settings.CMDS_DIR.glob("*.py"):
            if cmd_file.name !=  "__init__.py":
                await bot.load_extension(f"commands.{cmd_file.name[:-3]}")

        # await bot.load_extension("cogs.greetings")

    bot.run(settings.SECRET, root_logger=True)