import discord
import random
# import time
from discord.ext import commands

# CLIENT INITIATION
client = commands.Bot(command_prefix="//")

# ----------------------------------------------------#

# GENERAL DATABASE
nukeConfirm = ":arrows_counterclockwise: Channel is being nuked..."
noTextChannel = 'memes'

# ----------------------------------------------------#

# COMMAND DATABASE
about2 = 'This is a bot written by @Where did the cat go?#2609, specifically for testing purposes. New features will be added as soon as possible. A list of existing available commands can be found by typing //cmdhelp'
botOp = 'Where did the cats go?#2609'
info2: str = '__List of commands__:\n***//about*** - Information about the bot\n***//cmdhelp*** - List of commands\n***//nuke*** - Clears the channel history - NOT WORKING\n***//random*** - Random number between 1 and 10\n***//server*** - Server information\n\nIf you are having any problems DM me @Where did the cat go?#2690'
random2 = random.randint(1, 10)


# -----------------------------------------------------#
@client.command()
async def about(ctx):
    await ctx.send(about2)


@client.command()
async def cmdhelp(ctx):
    await ctx.send(info2)


@client.command()
async def info(ctx):
    await ctx.send(about2)


@client.command()
async def cmdlist(ctx):
    await ctx.send(info2)


'''@client.command()
async def nuke(ctx):
    await ctx.send(nukeConfirm)
    time.sleep(1)
    await channel.purge()'''


@client.command()
async def ping(ctx):
    await ctx.send(str(round(client.latency * 1000)) + 'ms')


@client.command()
async def random(ctx):
    await ctx.send(random2)


@client.command()
async def server(ctx):
    guildName = str(ctx.guild.name)
    guildOwner = str(ctx.guild.owner)
    guildId = str(ctx.guild.id)
    guildRegion = str(ctx.guild.region)
    guildMemberCount = str(ctx.guild.member_count)
    guildIcon = str(ctx.guild.icon_url)
    guildPing = str(round(client.latency * 1000)) + 'ms'
    guildEmbed = discord.Embed(
        title=guildName + ' Server Information',
        description='Information about the server',
        color=discord.Color.blue()
    )
    guildEmbed.set_thumbnail(url=guildIcon)
    guildEmbed.add_field(name="Server Owner", value=guildOwner, inline=True)
    guildEmbed.add_field(name="Server ID", value=guildId, inline=True)
    guildEmbed.add_field(name="Server Region", value=guildRegion, inline=True)
    guildEmbed.add_field(name="Server Ping", value=guildPing, inline=True)
    guildEmbed.add_field(name="Member Count", value=guildMemberCount, inline=True)
    await ctx.send(embed=guildEmbed)


client.run('Nzk0NTU1ODgwNDE0NzczMjQ4.X-8h1A.Qwi-3mbJESd_moG7MYganwO66OE') #THIS IS AN OLD OAUTH TOKEN THAT HAS BEEN REPLACED
