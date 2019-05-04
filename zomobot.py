import os
import discord
import json
import sys

# Reading in the information from config.json
try:
    with open('config.json') as json_data:
        config = json.load(json_data)
        json_data.close()
except:
    print("There was an error in opening \"./config.json\".\nPlease verify that you have correctly configured your file!")
    sys.exit()

# Initializing client and running Zomo!
client = discord.Client()
client.run(config["token"])