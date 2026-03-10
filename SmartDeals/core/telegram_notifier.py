import requests
import json

def send_alert(message):
    token = "7543829104:AAH_Example_Token" # استبدله بـ Token الخاص بك من BotFather
    chat_id = "8389318428" # معرفك الخاص الظاهر في لقطة الشاشة
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {"chat_id": chat_id, "text": message, "parse_mode": "HTML"}
    return requests.post(url, data=payload)

with open('products.json', 'r') as f:
    products = json.load(f)
    report = "🚀 <b>تقرير العنان للأسعار العالمية:</b>\n\n"
    for p in products:
        report += f"📱 <b>{p['name']}</b>\n💰 السعر: {p['price']}\n🏷️ {p['tag']}\n\n"

send_alert(report)
print("✅ النبضة وصلت إلى تيليجرام!")
