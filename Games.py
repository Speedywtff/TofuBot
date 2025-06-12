import random
import typing
import asyncio
import discord
from discord.ext import commands

class Games(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def flipcoin(self, ctx):
        await ctx.send(f"{random.choice(["tails", "heads"])}")
    
    @commands.command()
    async def roulette(self, ctx):
        author : discord.Member = ctx.author.mention
        if(len(ctx.message.mentions) == 0 or len(ctx.message.mentions) > 1):
            await ctx.send("You can only challenge 1 person!")
        opponent : list[discord.User] = ctx.message.mentions[0]
        if(author == opponent.mention):
            await ctx.send("You cannot challenge yourself!")
        else:


            await ctx.send(f"success! it is {author} vs {opponent.mention}")

            keepAlive = True
            roulette_outcomes = {
            0: "BANG! You're dead!",
            1: "Click! You're safe... for now.",
            2: "Click! You're safe... for now.",
            3: "Click! You're safe... for now.",
            4: "Click! You're safe... for now.",
            5: "Click! You're safe... for now.",
            }
            outcomes = list(roulette_outcomes.values())
            currentPlayer = author
            opponentPlayer = opponent.mention


            while True:
                choice = random.choice(outcomes)
                

                def check(msg):
                    return msg.content.lower() == "shoot" and msg.channel == ctx.channel and msg.author.mention == currentPlayer 

                try:
                    msg = await self.bot.wait_for("message", timeout=60, check = check) 
                except asyncio.TimeoutError:
                    await ctx.send(f"{currentPlayer} did not respond in time! {opponentPlayer} wins!")
                    break
                await ctx.send(choice)
            
                if choice == "BANG! You're dead!":
                    await ctx.send(f"{currentPlayer} has lost! {opponentPlayer} wins!")
                    break
                else:
                    outcomes.remove(choice)
                
                currentPlayer, opponentPlayer = opponentPlayer, currentPlayer

            
        
        
