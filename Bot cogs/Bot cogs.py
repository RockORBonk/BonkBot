import discord
import os
from discord.ext import commands

client = commands.Bot(command_prefix = 'bb!')

@client.command(aliases=["ul"])
@commands.is_owner()
async def load(ctx, extention):
    client.load_extension(f'cogs.{extention}')

@client.command()
@commands.is_owner()
async def unload(ctx, extention):
    client.unload_extension(f'cogs.{extention}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run('Nzk3MjE5MjkwMzE4NzY2MDgx.X_jSUg.08cIazAsiDbWJPeNrxSYks-5FMU')
