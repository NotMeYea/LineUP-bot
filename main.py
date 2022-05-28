import discord
from discord.ext import commands, tasks
from discord.utils import get, find

import os
import pathlib
import aiohttp
import datetime
import json

from config import CONFIG

intents = discord.Intents.default()
intents.presences = True
intents.members = True

client = commands.Bot(command_prefix = CONFIG.get("General", "Prefix"), intents=intents)


excluded_cogs = [""]


class Valorant_Lineup(commands.AutoShardedBot):
    def __init__(self):
        super().__init__(
            command_prefix=None,
            case_insensitive=True,
            description="Valorant_Lineup Discord bot.",
            intents=intents
        )

        self.token = CONFIG.get("General", "Token")

        self.load_cogs()


    def load_cogs(self):
        """Load cogs from the ./cogs/ folder."""
        cogs = [f"{p.parent}.{p.stem}" for p in pathlib.Path("cogs").glob("*.py")]

        print("\n┌─────────────────────────┐")

        for cog in [c for c in cogs if c not in excluded_cogs]:
            file_name = cog.split(".")[-1] + ".py"

            try:
                self.load_extension(cog)
            except Exception as e:
                print(f"├Error with {file_name}!\n" f"├  {e}")
            else:
                print(f"├Loaded cog: {file_name}")

    
    async def on_ready(self):
        await self.change_presence(status=discord.Status.online, activity=discord.Streaming(name="Valorant_Lineup", url="https://www.twitch.tv/Valorant_Lineupswithnothing%22"))
        print("|─────────────────────────|")
        print("Valorant_Lineup is online.")

        if not hasattr(self, "Uptime"):
            self.uptime = datetime.datetime.utcnow()

    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            embed = discord.Embed(
                title="Uh oh..",
                color=discord.Color(0x2f3136),
                description=f">>> ```fix\n{error}\n```",
                timestamp=ctx.message.created_at
            )
            embed.set_footer(text=f"Error raised by {ctx.message.author.name}")
            return await ctx.send(embed=embed)
        elif isinstance(error, commands.CheckFailure):
            return await ctx.send(error)

        raise error


    async def get_prefix(self, ctx):
        prefixes = [f"<@!{self.user.id}> ", f"<@{self.user.id}> "]
        prefixes.append(CONFIG.get("General", "Prefix"))
        return prefixes

    def run(self):
        super().run(self.token, reconnect=True)


if __name__ == "__main__":
    run = Valorant_Lineup()
    run.run()