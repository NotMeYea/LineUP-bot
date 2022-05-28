import discord
from discord.ext import commands

class Misc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def viperascent(self, ctx):
        await ctx.send("https://i.imgur.com/4fA9pcQ.png")
        await ctx.send("https://i.imgur.com/TZLa256.png")

    @commands.command()
    async def vipersplit(self, ctx):
        await ctx.send("https://i.imgur.com/ScuWjTu.png")
        await ctx.send("https://i.imgur.com/xmzMl89.png")

    @commands.command()
    async def viperfracture(self, ctx):
        await ctx.send("https://i.imgur.com/KFk95k2.png")
        await ctx.send("https://i.imgur.com/d1B6XND.png")

    @commands.command()
    async def viperbind(self, ctx):
        await ctx.send("https://i.imgur.com/SpehYus.png")
        await ctx.send("https://i.imgur.com/gxBuYgF.png")

    @commands.command()
    async def viperbreeze(self, ctx):
        await ctx.send("https://i.imgur.com/6d3UlXz.png")
        await ctx.send("https://i.imgur.com/6d3UlXz.png")

    @commands.command()
    async def vipericebox(self, ctx):
        await ctx.send("https://i.imgur.com/0Tgxvzk.png")
        await ctx.send("https://i.imgur.com/x4KJL4j.png")

    @commands.command()
    async def viperhaven(self, ctx):
        await ctx.send("https://i.imgur.com/ZOKKr0c.png")
        await ctx.send("https://i.imgur.com/HZQEqcs.png")
        await ctx.send("https://i.imgur.com/QmSVBen.png")


def setup(bot):
    bot.add_cog(Misc(bot))