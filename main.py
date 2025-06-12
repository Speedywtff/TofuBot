import discord
from discord import app_commands
from discord.ext import commands, tasks
import discord.utils
import random
from dotenv import load_dotenv
import os

load_dotenv()
token = os.getenv('TOKEN')
intents = discord.Intents.all()
client = discord.Client(intents=intents)
tree = discord.app_commands.CommandTree(client)



@client.event
async def on_ready():
    print(f"Logged in as {client.user.name} (ID: {client.user.id})")
    print("Tofu is online and ready to serve!")
    try:
        synced = await tree.sync()
        print(f"{len(synced)} commands synced.")
    except Exception as e:
        print(f"Error syncing commands: {e}")



@tree.command(name="hello", description="Says hello")
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message(f'Hello! how are you? (do not respond, my coder hasnt coded this) {interaction.user.mention}')

@tree.command(name="bye", description="Says bye")
async def bye(interaction: discord.Interaction):
    await interaction.response.send_message(f'Bye bye! Oh, wait. You arent leaving... {interaction.user.mention}')


#russian roulette
import asyncio


roulette_outcomes = {
    0: "BANG! You're dead!",
    1: "Click! You're safe... for now.",
    2: "Click! You're safe... for now.",
    3: "Click! You're safe... for now.",
    4: "Click! You're safe... for now.",
    5: "Click! You're safe... for now.",
}

@tree.command(name="roulette", description="Play a game of Russian Roulette against another user")
async def roulette(interaction: discord.Interaction, opponent: discord.Member):
    if opponent == interaction.user:
        await interaction.response.send_message("You can't play against yourself!")
        return

    await interaction.response.send_message(f"{interaction.user.mention} has challenged {opponent.mention} to a game of Russian Roulette!")

    outcomes = list(roulette_outcomes.values())
    current_player = interaction.user
    opponent_player = opponent

    while True:
        await interaction.channel.send(f"{current_player.mention}'s turn!")

        def check(msg):
            return msg.author == current_player and msg.channel == interaction.channel and msg.content.lower() == "shoot"

        try:
            msg = await interaction.client.wait_for("message", timeout=60, check=check)
        except asyncio.TimeoutError:
            await interaction.channel.send(f"{current_player.mention} didn't respond in time! {opponent_player.mention} wins!")
            break

        outcome = random.choice(outcomes)
        await interaction.channel.send(outcome)

        if outcome == "BANG! You're dead!":
            await interaction.channel.send(f"{current_player.mention} lost! {opponent_player.mention} wins!")
            break
        else:
            outcomes.remove(outcome)

        current_player, opponent_player = opponent_player, current_player


#coin flip
@tree.command(name= "flipcoin", description= "flips a coin")
async def flipcoin(interaction: discord.Interaction):
    await interaction.response.send_message (f'{random.choice(["tails", "heads"]) }')

#ping
@tree.command(name="ping", description="Returns the latency of the bot")
async def ping(interaction: discord.Interaction):
    await interaction.response.defer()
    latency = round(client.latency * 1000)
    await interaction.followup.send(content=f"Pong! Latency: {latency}ms")

client.run(token)