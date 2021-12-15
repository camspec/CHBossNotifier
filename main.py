import pause
import win32api
from datetime import datetime, time, timedelta, timezone


def utc_to_local(utc):
    return utc.replace(tzinfo=timezone.utc).astimezone(tz=None)


print("Successfully running")
while True:
    utcnow = datetime.utcnow()
    midnight = time(hour=0, minute=0)
    if utcnow.hour == 23 and utcnow.minute >= 50:
        pause.until(utc_to_local(datetime.combine(utcnow + timedelta(days=1), midnight)))
    designated_time = time(hour=23, minute=50)  # 23:50 UTC. boss ends at 23:55 and resets at 00:00, no dst
    designated_date = datetime.combine(datetime.utcnow(), designated_time)
    pause.until(utc_to_local(designated_date))
    win32api.MessageBox(0, "CH Boss ends in 5 minutes, resets in 10 minutes.", "ATTENTION!", 0x00001000)
