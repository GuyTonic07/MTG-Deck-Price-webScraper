#set up
from discord import Intents, Message
import discord
from discord.ext import commands
from dotenv import load_dotenv, find_dotenv
import os
from typing import Final
from Responses import get_response, get_deck_price

load_dotenv(find_dotenv())
TOKEN: Final = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True

#######################bot function#########################################

bot = commands.Bot(command_prefix="-", intents=intents, case_insensitive=True)


@bot.event
async def on_ready():
    channel = bot.get_channel(1222252767046013079)#bot testing channel
    print(f"Logged in as {bot.user}")
    await channel.send('Hello world ') 

@bot.command()
@commands.is_owner()
async def shutdown(ctx):
    channel = bot.get_channel(1222252767046013079)#bot testing channel
    await channel.send('logging off')
    await bot.close()
        
@bot.command()
async def Quote(ctx):
    response = get_response()
    await ctx.send(response)

@bot.command()
async def pricecheck(ctx, decklink: str):
    price = get_deck_price(decklink)  # Call the function from scraper.py
    
    if price:
        await ctx.send(f'Based on Card kingdom \nThe price of the deck is: {price}$')
    else:
        await ctx.send('Failed to retrieve the deck price. Please check the link and try again.')

###########################Error handling####################################
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CheckFailure) and ctx.command.name == 'shutdown':
        await ctx.send("You're not my owner!")
    else:
        raise error  # Re-raise the error so the default handler can handle it


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CheckFailure) and ctx.command.name == 'pricecheck':
        await ctx.send("I cannot find the price.")
    else:
        raise error  # Re-raise the error so the default handler can handle it
    
    
bot.run(TOKEN)
