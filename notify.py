import requests, os
from dotenv import load_dotenv
load_dotenv()
def send():
    msg = "🚀 *تمت السيطرة الكاملة!*\n✅ المجلد: SmartDeals\n✅ المزامنة: Force Push Success\n✅ البوت: متصل ومستعد."
    url = f"https://api.telegram.org/bot{os.getenv('TELEGRAM_TOKEN')}/sendMessage"
    requests.post(url, data={"chat_id": os.getenv("TELEGRAM_CHAT_ID"), "text": msg, "parse_mode": "Markdown"})
send()
