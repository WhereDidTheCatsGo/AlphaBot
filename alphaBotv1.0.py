import discord
import random
import time

# CLIENT INITIATION
client = discord.Client()

# ----------------------------------------------------#

# GENERAL DATABASE
nukeConfirm = ":arrows_counterclockwise: Channel is being nuked..."
noTextChannel = 'memes'

# ----------------------------------------------------#

# COMMAND DATABASE
aboutCmd = 'This is a bot written by @Where did the cat go?#2609, specifically for testing purposes. New features will be added as soon as possible. A list of existing available commands can be found by typing //help'
helpCmd = '__List of commands__:\n***//about*** - Information about the bot\n***//help*** - List of commands\n***//nuke*** - Clears the channel history\n***//ping*** - Returns the bot ping in milliseconds\n***//random*** - Random number between 1 and 10\n\nIf you are having any problems DM me @Where did the cat go?#2690'
randomCmd = random.randint(1, 10)
usersCmd = client.users


# -----------------------------------------------------#

@client.event
async def on_message(message):
    message.content = message.content.lower()
    if message.content.startswith('//about'):
        await message.channel.send(aboutCmd)

    if message.content.startswith('//help'):
        await message.channel.send(helpCmd)

    if message.content.startswith('//info2'):
        await message.channel.send(aboutCmd)

    if message.content.startswith('//list'):
        await message.channel.send(helpCmd)

    if message.content.startswith('//random'):
        await message.channel.send(randomCmd)

    if message.content.startswith('//nuke'):
        await message.channel.send(nukeConfirm)
        time.sleep(1)
        await message.channel.purge()

    if message.content.startswith('//lenny'):
        await message.edit.content[str('( ͡° ͜ʖ ͡°)')]

    if "memes" == str(message.channel) and message.content != "":
        await message.channel.purge(limit=1)

    if message.content.startswith('//ping'):
        await message.channel.send({round(client.latency * 1000)})


client.run('Nzk0NTU1ODgwNDE0NzczMjQ4.X-8h1A.PjJs54z1c9VKpjylzSnEKjEkka4') #THIS IS AN OLD OAUTH TOKEN WHICH HAS BEEN REPLACED
