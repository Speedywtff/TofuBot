import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
from Games import Games



load_dotenv()
token = os.getenv('TOKEN')
intents = discord.Intents.all()
bot = commands.Bot(command_prefix = '.', intents = intents)



@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name} (ID: {bot.user.id})")
    print("Tofu test is online and ready to serve!")
    try:
        await bot.add_cog(Games(bot))
        synced = len(bot.commands)
        print(f"{synced} commands synced.")
    except Exception as e:
        print(f"Error syncing commands: {e}")



@bot.command()
async def ping(ctx):
    latency = round(bot.latency * 1000)
    await ctx.send(content=f"Pong! Latency: {latency}ms")

@bot.command()
async def hello(ctx):
    await ctx.send(content = f"Hello, {ctx.author.mention}! how are you?")

@bot.command()
async def bye(ctx):
    await ctx.send(content = f"Bye bye, {ctx.author.mention}! Oh, wait. You arent leaving...")



bot.run(token)