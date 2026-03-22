import requests
import os

def send_mission_report(status_message):
    TOKEN = "8013568115:AAHHXylAt5ibZEpJ53wSfkXWOh-pzdVDth4"
    # استبدل 123456789 بـ Chat ID الخاص بك (يمكنك الحصول عليه من @userinfobot)
    CHAT_ID = "8389318428" 
    
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": f"🚀 **Benalal AI Core v2.0**\n\n🛡️ Status: {status_message}\n📅 Time: 2026-03-22\n✅ GitHub Sync: Verified",
        "parse_mode": "Markdown"
    }
    try:
        requests.post(url, json=payload)
    except:
        pass
