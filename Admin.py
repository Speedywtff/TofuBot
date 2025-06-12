import typing
import discord
from discord.ext import commands

class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            await ctx.send(f"Command not found!")
            return
    
    @commands.command()
    @commands.has_permissions(manage_channels = True)
    async def ignore_channel(self, ctx, channel : discord.TextChannel):
        await ctx.send(f"ignoring: {channel.mention}")
#tofinish


