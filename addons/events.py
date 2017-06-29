import discord
from discord.ext import commands
import git

git = git.cmd.Git(".")

class Events:
    """Event handling."""

    def __init__(self, bot):
        self.bot = bot
        print('Addon "{}" loaded'.format(self.__class__.__name__))

    async def on_message(self, message):
        #auto update
        if message.author.name == "GitHub" and message.author.discriminator == "0000":
            print("Pulling changes!")
            git.pull()
            print("Changes pulled!")

    async def on_member_join(self, member):
        try:
            await self.bot.send_message(member, "Welcome to Lucario101's emote server! Please read our {} and have fun!".format(self.bot.rules_channel.mention))
        except discord.errors.Forbidden: # doesn't accept DMs from non-friends
            pass
        await self.bot.add_roles(member, self.bot.idiots_role)
        await self.bot.send_message(self.bot.logs_channel, ":exclamation: Member joined: {}#{}".format(member.name, member.discriminator))

    async def on_member_remove(self, member):
        await self.bot.send_message(self.bot.logs_channel, ":exclamation: Member left: {}#{}".format(member.name, member.discriminator))

    async def on_member_ban(self, member):
        await self.bot.send_message(self.bot.logs_channel, ":exclamation: Member banned: {}#{}".format(member.name, member.discriminator))

    async def on_member_unban(self, server, member):
        await self.bot.send_message(self.bot.logs_channel, ":exclamation: Member unbanned: {}#{}".format(member.name, member.discriminator))

def setup(bot):
    bot.add_cog(Events(bot))
