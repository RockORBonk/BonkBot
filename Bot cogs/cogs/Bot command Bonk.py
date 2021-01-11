import discord
from discord.ext import commands
import datetime
import asyncio



from PIL import Image
from io import BytesIO

class Bonk(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Bonk Bot is online')

    @commands.command()
    async def bonk(self, ctx, user: discord.Member = None):
        if user == None:
            user = ctx.author
        
            bonk = Image.open("Bonk.jpg", "r")

            asset = user.avatar_url_as(size = 128)
            data = BytesIO(await asset.read())
            pfp = Image.open(data)

            pfp = pfp.resize((343,343))

            bonk.copy()

            bonk.paste(pfp, (158,229))

            bonk.save("bonk1.jpg")
            a = await ctx.send(file=discord.File('bonk1.jpg'))
    
            await asyncio.sleep(3)

            await a.delete()


#Bonk 2

            bonk = Image.open("Bonkframe2.jpg")

            asset = user.avatar_url_as(size = 128)
            data = BytesIO(await asset.read())
            pfp = Image.open(data)

            pfp = pfp.resize((260,278))

            bonk.copy()

            bonk.paste(pfp, (195,255))

            bonk.save("bonk2.jpg")
            await ctx.send(file=discord.File('bonk2.jpg'))

def setup(client):
    client.add_cog(Bonk(client))



