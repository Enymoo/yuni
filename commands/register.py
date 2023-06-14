from discord.ext import commands
import random, discord, mysql.connector as db, settings

@commands.command(
    help = "This is help",
    description = "This is description",
    brief = "This is brief"
)
async def register(ctx):
    try:
        connection = db.connect (
            host=settings.HOST,
            user=settings.USER,
            password=settings.PASSWORD,
            database=settings.DATABASE
        )
        with connection.cursor(dictionary=True) as cursor:
            sql = "SELECT * FROM users WHERE userid=%s"
            values = ctx.author.id
            cursor.execute(sql, (values,))

            rows = cursor.fetchall()
            if rows:
                await ctx.reply("You are already registed!")
                raise Exception("You are already registered!")

            sql = "INSERT INTO users (userid, balance) VALUES (%s, %s)"
            values = (int(ctx.author.id), 0)
            cursor.execute(sql, values) 
            
            connection.commit()
            cursor.close()
            connection.close()

        await ctx.reply("You have been registered!")
    except Exception as e:
        print(str(e))
    
async def setup(bot):
    bot.add_command(register)