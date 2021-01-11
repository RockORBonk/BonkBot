import discord
from discord.ext import commands

class Example(commands.Cog):

    def __init__(self, client):
        self.client = client
#Events

    @commands.Cog.listener()
    async def on_ready(self):
        print('Bonk Bot is online')

#Commands
    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f':ping_pong: {round(self.client.latency * 1000)}ms')

def setup(client):
    client.add_cog(Example(client))