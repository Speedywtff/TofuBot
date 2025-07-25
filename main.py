import discord
from discord.ext import commands
import os
from Games import Games
from Admin import Admin
from Random import Random
from Ticket import Ticket




token = os.environ.get('token')
intents = discord.Intents.all()



bot = commands.Bot(command_prefix = '.', intents = intents)



@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name} (ID: {bot.user.id})")
    print("Tofu test is online and ready to serve!")
    try:
        await bot.add_cog(Games(bot))
        await bot.add_cog(Admin(bot))
        await bot.add_cog(Random(bot))
        await bot.add_cog(Ticket(bot))
        synced = len(bot.commands)
        print(f"{synced} commands synced.")
    except Exception as e:
        print(f"Error syncing commands: {e}")


@bot.event
async def on_member_join(member : discord.Member):
    icon = member.display_avatar.url
    embed = discord.Embed(
        colour = discord.Color.dark_teal(),
        title = "New member",
        description= f"Welcome {member.mention}, We hope you have a great time here!"
    )
    embed.set_thumbnail(url=icon)
    embed.set_image(url="https://i.imgur.com/r0iaDTY.png")

    channel = bot.get_channel(1382292647074336861)

    await channel.send(embed=embed)



bot.run(token)
