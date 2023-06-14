from discord.ext import commands
from user import User
import discord, mysql.connector as db, settings

@commands.group(
    help = "This is help",
    description = "This is description",
    brief = "This is brief"
)
async def profile(ctx, member: discord.Member = None):
    connection = None
    user = None

    try:
        connection = db.connect (
            host=settings.HOST,
            user=settings.USER,
            password=settings.PASSWORD,
            database=settings.DATABASE
        )

    except Exception as e:
        print(str(e))

    if member == None:
        try:
            with connection.cursor() as cursor:
                sql = "SELECT * FROM users WHERE userid=%s"
                value = ctx.author.id
                cursor.execute(sql, (value,))
                result = cursor.fetchall()[0]
                user = User(result[0], result[1], result[2])
        except Exception as e:
            print(str(e))   

        embed = discord.Embed(
            color=discord.Color.from_str(user.color)
        )

        # Add fields to the embed
        embed.add_field(name="Balance", value=f"$ {user.balance}", inline=False)

        # Set the author and footer of the embed
        embed.set_author(name=f"{ctx.author.display_name}'s profile", icon_url=ctx.author.avatar)
        embed.set_footer(text=f"{ctx.author.id} | made by @enymu")

        await ctx.send(embed=embed)

@profile.command()
async def color(ctx, color):
    pass 

async def setup(bot):
    bot.add_command(profile)