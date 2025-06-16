import discord
from discord.ext import commands
import os
from Games import Games
from Admin import Admin
from Random import Random
from CustomHelp import CustomHelpCommand



token = os.environ.get('token')
intents = discord.Intents.all()



bot = commands.Bot(command_prefix = '.', intents = intents, help_command=CustomHelpCommand())



@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name} (ID: {bot.user.id})")
    print("Tofu test is online and ready to serve!")
    try:
        await bot.add_cog(Games(bot))
        await bot.add_cog(Admin(bot))
        await bot.add_cog(Random(bot))
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
    embed.set_image(url="https://www.shutterstock.com/shutterstock/photos/1146069941/display_1500/stock-vector-welcome-poster-with-spectrum-brush-strokes-on-white-background-colorful-gradient-brush-design-1146069941.jpg")

    channel = bot.get_channel(1382587220048875520)

    await channel.send(embed=embed)



bot.run(token)