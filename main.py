#Made by GuyTonic/Corey 
from discord import Intents, Message
import discord
from discord.ext import commands
from dotenv import load_dotenv, find_dotenv
import os
from typing import Final
from Responses import get_response, get_deck_priceArch, get_deck_price_tapped
from Sel import get_deck_price_moxfield


load_dotenv(find_dotenv()) #This is where the discord Token his hidden yall can't have this
TOKEN: Final = os.getenv('DISCORD_TOKEN')


intents = discord.Intents.default() 
intents.message_content = True

#########################################bot function#########################################

bot = commands.Bot(command_prefix="-", intents=intents, case_insensitive=True)


@bot.event # on bot start up
async def on_ready():
    channel = bot.get_channel(1222252767046013079) #bot testing channel
    print(f"Logged in as {bot.user}")
    await channel.send('Hello world ') 

@bot.command() #Shut down command
@commands.is_owner()
async def shutdown(ctx):
    channel = bot.get_channel(1222252767046013079) #bot testing channel
    await channel.send('logging off')
    await bot.close()
        
@bot.command() #for the !quote command
async def Quote(ctx):
    response = get_response()
    await ctx.send(response)

@bot.command() #this set of commands control the webscrapper 
async def pricecheck(ctx, decklink: str):
    if 'scryfall.com' in decklink: #Scryfall NOT YET SUPPORTED
        await ctx.send('I do not Support this yet, please ask <@645314806051766272>') #owners ID

async def pricecheck(ctx, decklink: str):    
    if 'deckstats.net' in decklink: #DeckStats NOT YET SUPPORTED 
        await ctx.send('I do not Support this yet, please ask <@645314806051766272>')#owners ID
    
    elif 'moxfield.com' in decklink: #MoxField SUPPORTED
        price = get_deck_price_moxfield(decklink) #Calls to Sel Function
        if price:
            await ctx.send(f'Based on card kingdom \nThe price of the deck is: {price}$')
    
    elif 'archidekt.com' in decklink: #Archidekt SUPPORTED 
        price = get_deck_priceArch(decklink)  #Calls to Soup Function
        if price:
            await ctx.send(f'Based on Card kingdom \nThe price of the deck is: {price}$')

        else:
            await ctx.send('Failed to retrieve the deck price from Archidekt. Please check the link and try again.')
        
    elif 'tappedout.net' in decklink: #Tappedout SUPPORTED
        prices = get_deck_price_tapped(decklink) #Calls to soup Function
        
        prices1 = prices[0]
            
        prices2 = prices[1]
        
        if prices:
            if len(prices1) == 2:
                await ctx.send(f'Based on Card kingdom \nThe price of the deck is: {prices1[0]}$' + '-' + prices1[1] + '$\n'
                            f'Based on TCGplayer \nThe price of the deck is: {prices2[0]}$' + '-' + prices2[1] + '$')
            elif len(prices1) == 1:
                await ctx.send(f'Based on Card kingdom \nThe price of the deck is: {prices1[0]}$' +'\n'
                            f'Based on TCGplayer \nThe price of the deck is: {prices2[0]}$' + '-' + prices2[1] + '$')
                
        else:
            await ctx.send('Failed to retrieve the deck price from Tappedout. Please check the link and try again.')

###########################Error handling####################################
@bot.event
async def on_command_error(ctx, error): #this is the command to stop the bot from running only I (the owner) can excute this
    if isinstance(error, commands.CheckFailure) and ctx.command.name == 'shutdown':
        await ctx.send("You're not my owner!")
    else:
        raise error  


@bot.event
async def on_command_error(ctx, error): #in the case of a price now coming back this will launch
    if isinstance(error, commands.CheckFailure) and ctx.command.name == 'pricecheck':
        await ctx.send("I cannot find the price.")
    else:
        raise error 
    
    
bot.run(TOKEN)
