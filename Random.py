import discord
from discord.ext import commands

class Random(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(brief = "Test bots latency")
    async def ping(self, ctx):
        latency = round(self.bot.latency * 1000)
        await ctx.send(content=f"Pong! Latency: {latency}ms")

    @commands.command(brief = "Nice hello message!")
    async def hello(self, ctx):
        await ctx.send(content = f"Hello, {ctx.author.mention}! how are you?")

    @commands.command(brief = "Bye bye!")
    async def bye(self, ctx):
        await ctx.send(content = f"Bye bye, {ctx.author.mention}! Oh, wait. You arent leaving...")