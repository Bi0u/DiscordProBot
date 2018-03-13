import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time

Client = discord.Client()
client = commands.Bot (command_prefix = "!")

@client.event
async def on_ready():
        print("Bot is ready!!")

@client.event
                #BULBASSAUR

async def on_message(Bulbassaur):
    if Bulbassaur.content.startswith('!Bulbassaur_Info'):
	passw = '0'    
        userID = Bulbassaur.author.id
        userInput = Bulbassaur.content
        await client.send_message(Bulbassaur.channel, "What would you like to know about Bulbassaur? <@%s>" % (userID))
    if Bulbassaur.content == "!Evolutions":
        await client.send_message(Bulbassaur.channel, ":Bulbassaur: Evolutions.")
        await client.send_file(Bulbassaur.channel, r'C:\Users\vmrc2\Desktop\Pro Bot\Bulbassaur_Evolutions.png')
                

async def on_message(message):        
    if message.content == "Hi":
        userID = message.author.id
        await client.send_message(message.channel, "Hi! <@%s>" % (userID))
    if message.content.startswith('!server_status'):
        userID = message.author.id
        await client.send_message(message.channel, "<@%s> Everything ok!" % (userID))
    if message.content.startswith('!pokemons'):
         args = message.content.split(" ")
         #args[0] = !pokemons
         #args[1] = I Like 
         #args[2] = Pikachu
         #args[1:] = I Like Pikachu
         await client.send_message(message.channel, "%s" % (" ".join(args[1:])))

client.run("NDIyMTE1MDM4MjI5Mjk5MjEw.DYYOrA.3DWFx3LFk3LZyN6gk-Kz9KgxQhY")

