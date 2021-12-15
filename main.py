import pause
import win32api
from discord_webhook import DiscordWebhook
from datetime import datetime, time, timedelta, timezone
import os


def utc_to_local(utc):
    return utc.replace(tzinfo=timezone.utc).astimezone(tz=None)


if not os.path.isfile("./webhookurl.txt"):
    url = input("Paste webhook url: ")
    with open("webhookurl.txt", "w") as file:
        file.write(url)
    webhook = DiscordWebhook(url=url, content="CH Boss ends in 5 minutes, resets in 10 minutes.")
else:
    with open("webhookurl.txt") as file:
        webhook = DiscordWebhook(url=file.readlines(), content="CH Boss ends in 5 minutes, resets in 10 minutes.")
        print("*To change your webhook url, edit webhookurl.txt*")    

print("Successfully running")
while True:
    utcnow = datetime.utcnow()
    midnight = time(hour=0, minute=0)
    if utcnow.hour == 23 and utcnow.minute >= 50:
        pause.until(utc_to_local(datetime.combine(utcnow + timedelta(days=1), midnight)))
    designated_time = time(hour=23, minute=50)  # 23:50 UTC. boss ends at 23:55 and resets at 00:00, no dst
    designated_date = datetime.combine(datetime.utcnow(), designated_time)
    pause.until(utc_to_local(designated_date))
    response = webhook.execute()
    win32api.MessageBox(0, "CH Boss ends in 5 minutes, resets in 10 minutes.", "ATTENTION!", 0x00001000)
