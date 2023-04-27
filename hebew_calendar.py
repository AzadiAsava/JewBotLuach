
from datetime import datetime
from pyluach import dates
import datetime
from astral import LocationInfo
from astral.sun import sun

def get_current_holiday() -> str:
    
    now = datetime.datetime.now()
    # Calculate the next Friday at sunset
    friday = now + datetime.timedelta((4 - now.weekday()) % 7)
    loc = LocationInfo(name='SJC', region='CA, USA', timezone='America/Los_Angeles',
                   latitude=37.3713439, longitude=-121.944675)
                   
    s = sun(loc.observer, date=friday, tzinfo=loc.timezone)

    sunset = s['sunset']
    friday_sunset = datetime.datetime(friday.year, friday.month, friday.day, sunset.hour, sunset.minute, sunset.second)
    saturday_sunset = friday_sunset + datetime.timedelta(days=1)
    
    next_candle = friday_sunset - datetime.timedelta(minutes=18) # Assumes candles are lit 18 minutes before sunset
    havdalah = saturday_sunset + datetime.timedelta(minutes=42) # Assumes 42 minutes after sunset

    # Print the next candle lighting and Havdalah times
    return "The next candle lighting time is: " + next_candle.strftime("%A, %B %d, %Y at %I:%M %p") + "\nThe next Havdalah time is: " + havdalah.strftime("%A, %B %d, %Y at %I:%M %p")

print(get_current_holiday())