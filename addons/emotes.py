import discord
from discord.ext import commands
import os
import sys

class Utility:
    """Emote management."""
    def __init__(self, bot):
        self.bot = bot
        print('Addon "{}" loaded'.format(self.__class__.__name__))  
    
    @commands.has_permissions(manage_emojis=True)
    @commands.command(pass_context=True, aliases=['emote'])
    async def emoji(self, ctx, emoji_name, image_url):
        """Add an emoji to the server from a URL."""
        image = requests.get(image_url, stream=True)
        await self.bot.create_custom_emoji(ctx.message.server, name=emoji_name, image=image)  
        await self.bot.say("Successfully added the {} emoji to the server!".format(emoji_name))
        
def setup(bot):
    bot.add_cog(Utility(bot))