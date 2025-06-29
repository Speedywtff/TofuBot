import discord
from discord.ext import commands

class ticketbutton(discord.ui.View):
    @discord.ui.button(label = "Start a ticket", style=discord.ButtonStyle.primary)
    async def button_callback(self, interaction: discord.Interaction, button: discord.ui.Button):
        
        guild = interaction.guild
        message = f"{interaction.user}s Ticket"
        channelnew = await guild.create_text_channel(name = message, category = discord.utils.get(guild.categories, id = 1388664502727475321))

        embed = discord.Embed(
            colour = discord.Color.dark_embed(),
            title = "Registered ticket",
            description= f"Please refer to this channel: <#{channelnew.id}>",
        )
        await interaction.response.send_message(ephemeral = True, embed = embed)

        newEmbed = discord.Embed(
            colour = discord.Color.blue(),
            title = "Ticket opened.",
            description= "Wait for a staff member to get back to you. It may take a while!",
        )

        await channelnew.send(embed = newEmbed)

        staffEmbed = discord.Embed(
            color = discord.Color.red(),
            title = "New Ticket",
            description= f"hey <@&1382488946507776000>, {interaction.user.mention} just opened a new ticket in: <#{channelnew.id}>. Remember, .close will close the ticket and send it to the closed tickets category",
        )

        staff = guild.get_channel(1388676915673432224)

        await staff.send(embed = staffEmbed)
        


class Ticket(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    

    @commands.command(brief = "Initiate ticket!")
    async def startTicket(self, ctx):
        embed = discord.Embed(
            color = discord.Color.dark_magenta(),
            title = "Tickets",
            description= "Click on the reaction below to start a ticket!",
        )
        await ctx.send(embed = embed, view = ticketbutton())
    
    @commands.has_role(1388671405859672176)
    @commands.command(brief = "closes a ticket channel.")
    async def close(self, ctx):
        if ctx.channel.category_id == 1388664502727475321:
            closed = discord.utils.get(ctx.guild.categories, id = 1388664546801094717)
            await ctx.channel.edit(category = closed)
        else:
            await ctx.send("This command does not work on text channels in this category!")


