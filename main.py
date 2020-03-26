import discord
from discord.ext import commands
from zidane_msg import get_random_quote

client = commands.Bot(command_prefix = '!')

@client.event
async def on_ready():
    print('Bonjour its Michel ')


@client.event
async def on_member_join(member):
    msg = 'Salut {member}, tu aimes jouer au foot ?'
    await client.send_message("general", msg)


@client.command()
async def zidane(ctx):
    msg = get_random_quote()
    await ctx.send(msg)


@client.event
async def on_message(message):
    if not message.author.id == 646757160491155466:
        if 'zidane' in message.content.lower():
            msg = get_random_quote()
            await message.channel.send(msg)

client.run('NjQ2NzU3MTYwNDkxMTU1NDY2.XdVx6Q.htPSN1GVyEoxh-DFs6TD2K3ZgA8')