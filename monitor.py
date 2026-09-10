import os
import requests
from datetime import datetime, timezone

USERNAME = os.environ["IG_USERNAME"]
WEBHOOK = os.environ["DISCORD_WEBHOOK"]

url = f"https://www.instagram.com/{USERNAME}/"

try:
    r = requests.get(
        url,
        headers={"User-Agent": "Mozilla/5.0"},
        timeout=15
    )

    if r.status_code == 200:
        status = "🟢 ACCESSIBLE"
    elif r.status_code in (401, 403, 404):
        status = "🔴 UNAVAILABLE"
    else:
        status = f"🟡 CHECK FAILED ({r.status_code})"

    now = datetime.now(timezone.utc).strftime("%d %b %Y, %H:%M:%S UTC")

    message = (
        f"**Instagram Monitor**\n"
        f"👤 @{USERNAME}\n"
        f"📊 Status: {status}\n"
        f"🕐 Checked: {now}"
    )

    requests.post(
        WEBHOOK,
        json={"content": message},
        timeout=15
    )

except Exception as e:
    print("Error:", e)
