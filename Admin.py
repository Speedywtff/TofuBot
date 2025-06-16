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
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Please pass in all requirements :rolling_eyes:.')
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You dont have all the requirements :angry:")
    
    
    @commands.command()
    @commands.has_permissions(manage_channels = True)
    async def ignore_channel(self, ctx, channel : discord.TextChannel):
        await ctx.send(f"ignoring: {channel.mention}")
#tofinish

    @commands.command()
    @commands.has_permissions(ban_members = True)
    async def ban(self, ctx, member : discord.Member, *, reasonBanned : str = None):
        try:
            if not ctx.guild.me.guild_permissions.ban_members:
                await ctx.send("**I cannot ban members!**")
                return

            await member.ban(reason=reasonBanned)

            channel = self.bot.get_channel(1382500608522584135)
            
            if channel:
                await channel.send(f"{member} has been banned for reason: {reasonBanned}.")
            else:
                await ctx.send(f"{member} has been banned for reason: {reasonBanned}.")

        except discord.NotFound:
            await ctx.send("**Member not found.**")
        except discord.Forbidden:
            await ctx.send("**You do not have the required permissions for this command**")
        except discord.HTTPException:
            await ctx.send("**Unknown error occured. Please try again.**")
        except TypeError:
            await ctx.send("**Commands arguments are not as expected.**")
        except Exception as e:
            print(e)
            await ctx.send("**Unknown error occurred. Please try again**")
    
    @commands.command(description = "Unbans member. Usage: <prefix>unban <@UserId> reason. reason is optional")
    @commands.has_permissions(ban_members = True)
    async def unban(self, ctx, member: discord.User, *, reasonUnban : str = None):
        try:
            if not ctx.guild.me.guild_permissions.ban_members:
                await ctx.send("**I cannot unban members!**")
                return
            await ctx.guild.unban(member, reason=reasonUnban)
            await ctx.send(f"{member} unbanned!")
        except discord.NotFound:
            await ctx.send("**Member either not found or was not in the ban list.**")
        except discord.Forbidden:
            await ctx.send("**You do not have the required permissions for this command**")
        except discord.HTTPException:
            await ctx.send("**Unknown error occured. Please try again.**")
        except Exception as e:
            print(e)
    
    @commands.command()
    async def can_ban(self, ctx):
        try:
            if ctx.author.guild_permissions.ban_members:
                await ctx.send("You can ban!")
            else:
                await ctx.send("You cannot ban!")
        except Exception as e:
            print(e)


