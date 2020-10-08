import discord
import os
import markov
import sys

DISCORD_TOKEN = os.environ['DISCORD_TOKEN']

filenames = sys.argv[1:]

# Open the files and turn them into one long string
text = markov.open_and_read_file(filenames)

# Get a Markov chain
chains = markov.make_text(markov.make_chains(text))

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('hello'):
        await message.channel.send(markov.make_text(markov.make_chains(text)))


client.run(DISCORD_TOKEN)