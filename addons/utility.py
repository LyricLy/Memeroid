import discord
from discord.ext import commands
import os
import sys

class Utility:
    """Utility bot commands."""
    def __init__(self, bot):
        self.bot = bot
        print('Addon "{}" loaded'.format(self.__class__.__name__))  
    
    @commands.command()
    async def test(self):
        """A test command."""
        embed = discord.Embed(title="Testing", description="This is a test message!")
        embed.add_field(name="More testing", value="This is a test field!", inline=False)
        embed.colour = discord.Colour(0x00FFFF)            
        await self.bot.say("", embed=embed)
    
    @commands.has_permissions(ban_members=True)    
    @commands.command()
    async def restart(self):
        """Restarts the bot."""
        await self.bot.say("Restarting...")
        os.execv(sys.executable, ['python3.6'] + sys.argv)
        
def setup(bot):
    bot.add_cog(Utility(bot))