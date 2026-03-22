import subprocess
import json

def get_latest_deal():
    username = "@tvbenalal"
    url = f"https://www.tiktok.com/{username}"
    cmd = [
        "yt-dlp",
        "--quiet",
        "--no-warnings",
        "--get-id",
        "--playlist-items", "1",
        url
    ]
    try:
        video_id = subprocess.check_output(cmd).decode('utf-8').strip()
        if video_id:
            return {
                "title": "New Smart Deal Detected",
                "url": f"https://www.tiktok.com/@tvbenalal/video/{video_id}"
            }
    except:
        return None
