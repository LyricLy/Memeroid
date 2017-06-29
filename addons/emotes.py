import discord
import requests
from discord.ext import commands
import os
import sys

class Utility:
    """Emote management."""
    def __init__(self, bot):
        self.bot = bot
        print('Addon "{}" loaded'.format(self.__class__.__name__))  
    
    @commands.has_permissions(manage_emojis=True)
    @commands.command(aliases=['emote'])
    async def emoji(self, emoji_name, image_url):
        """Add an emoji to the server from a URL."""
        image = requests.get(image_url, stream=True)
        await self.bot.create_custom_emoji(self.bot.server, name=emoji_name, image=image.content)  
        await self.bot.say("Successfully added the {} emoji to the server!".format(emoji_name))
        
def setup(bot):
    bot.add_cog(Utility(bot))