import typing
import discord
from discord.ext import commands

class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def ignore_channel(self, ctx):
        await ctx.send("hello")