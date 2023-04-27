import discord
from discord.ext import commands
from datetime import datetime
from pyluach import dates, hebrewcal, parshios
import os

# Create a new Discord bot client

intents = discord.Intents.default()
intents.members = True
intents.guilds = True
intents.bans = True
intents.emojis = True
intents.reactions = True
intents.typing = True
client = commands.Bot(command_prefix='!', intents=intents)

# Define a command to get the holiday information
@client.command()
async def holiday(ctx, holiday_name):
    # Get the current year
    current_year = datetime.now().year
    
    # Get the date and times for the requested holiday
    holiday_date = dates.HebrewDate.today().get_holiday_date(holiday_name, year=current_year)
    candle_lighting_time = holiday_date.get_candle_lighting()
    havdalah_time = holiday_date.get_havdalah()

    # Format the response message
    message = f"**{holiday_name}** is on {holiday_date.to_pydate().strftime('%A, %B %d, %Y')}.\nCandle lighting time is at {candle_lighting_time}.\nHavdalah time is at {havdalah_time}."

    # Send the message to the Discord channel
    await ctx.send(message)

# Run the bot
client.run(os.environ.get('JewBotLuachDiscordToken'))


