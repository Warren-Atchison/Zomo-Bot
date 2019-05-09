import os
import discord
import json
import sys
import RandomSmite

# Reading in the information from config.json
try:
    with open('config.json') as json_data:
        config = json.load(json_data)
        json_data.close()
except:
    print("There was an error in opening \"./config.json\".\nPlease verify that you have correctly configured your file!")
    sys.exit()

# Initializing client
client = discord.Client()

# Reading every message sent in a channel Zomo monitors
@client.event
async def on_message(message):

    # Filters out messages sent by bots (including Zomo)
    if(message.author.bot):
        return

    # Sends a greeting on "<prefix>hi"
    if(message.content == (config["prefix"] + "hi")):
        await message.channel.send("Hi! :heart:")
    # Run the Random Smite app
    elif(message.content[0] == "%"):
        RandomSmite.main()
        

# Start Zomo!
client.run(config["token"])
