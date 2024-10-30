import os
import importlib
from discord import Intents, Client
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents: Intents = Intents.default()
intents.message_content = True

PREFIXES = ['!', '?']
client: Client = commands.Bot(command_prefix=PREFIXES, intents=intents, help_command=None)

async def load_cogs(client):
    cogs_directory = "cogs"
    for filename in os.listdir(cogs_directory):
        if filename.endswith(".py"):
            cog_name = filename[:-3]
            try:
                importlib.import_module(f"{cogs_directory}.{cog_name}")
                await client.load_extension(f"{cogs_directory}.{cog_name}")
            except Exception as e:
                print(f"Failed to load extension {cog_name}.")
                print(e)

@client.event
async def on_ready() -> None:
  print(f'Logged in as {client.user}!')
  await load_cogs(client)

client.run(TOKEN)