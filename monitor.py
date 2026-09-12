import os
import requests
from datetime import datetime, timezone, timedelta

username = os.environ["INSTAGRAM_USERNAME"]
webhook = os.environ["DISCORD_WEBHOOK"]

url = f"https://www.instagram.com/{username}/"

headers = {
    "User-Agent": "Mozilla/5.0"
}

try:
    r = requests.get(url, headers=headers, timeout=15)

    if r.status_code == 200:
        ist = timezone(timedelta(hours=5, minutes=30))
        now = datetime.now(ist).strftime("%d %b %Y, %I:%M:%S %p")

        message = (
            "🔔 Instagram account accessible!\n"
            f"👤 @{username}\n"
            f"🕐 Detected: {now} IST"
        )

        requests.post(
            webhook,
            json={"content": message},
            timeout=15
        )

except Exception as e:
    print("Check failed:", e)
