import discord
import requests
import sys
import os
import traceback
import jishaku
from discord.ext import commands, tasks
from dotenv import load_dotenv
from itertools import cycle
from keep_alive import keep_alive

intents = discord.Intents.all()
intents.members = True
bot = commands.Bot(command_prefix="d!", intents=intents)
#bot.remove_command('help')
status = cycle([discord.Activity(type=discord.ActivityType.watching, name="TSK Verified Discord Server"), discord.Activity(type=discord.ActivityType.listening, name="TSK Verified")])

@bot.event
async def on_ready():
  change_status.start()
  print("DNA is online")
  channel = bot.get_channel(822873485532463114)
  await channel.send("DNA is online")

@tasks.loop(seconds=5)
async def change_status():
  await bot.change_presence(activity=next(status))

bot.owner_ids=[651506861844987906, 699566190842085439]

extensions = ['cogs.moderation',
              'cogs.fun',
							'cogs.event',
              'cogs.info',
              'cogs.utility',
              'cogs.api',
              'cogs.chat'
]
if __name__ == '__main__':
  for extension in extensions:
    try:
      bot.load_extension(extension)
    except Exception as e:
      print(f"Error loading {extension}", file=sys.stderr)
      traceback.print_exc()

keep_alive()
bot.load_extension("jishaku")
bot.run(os.env['TOKEN'])
