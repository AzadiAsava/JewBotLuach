import discord
from discord.ext import commands
from datetime import datetime
from pyluach import dates, hebrewcal, parshios
import os
import hebew_calendar
# Create a new Discord bot client

intents = discord.Intents(messages=True, guilds=True, message_content=True, members=True, guild_reactions=True, dm_reactions=True, presences=True, reactions=True, typing=True, voice_states=True, webhooks=True)
client = commands.Bot(command_prefix='!', intents=intents)

# Define a command to get the holiday information
@client.command()
async def holiday(ctx, holiday_name):
    message = hebew_calendar.get_current_holiday()
    # Send the message to the Discord channel
    await ctx.send(message)

# Run the bot
client.run(os.environ.get('JewBotLuachDiscordToken'))


