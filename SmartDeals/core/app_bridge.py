from flask import Flask, request
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

# 🔑 الإعدادات الأمنية - استبدل YOUR_TOKEN بتوكن بوتك الحقيقي
TOKEN = "YOUR_API_TOKEN_HERE" 
CHANNEL_ID = "@mSmartDeals_MA"

@app.route('/send_ad', methods=['POST'])
def send_ad():
    data = request.json
    msg = data.get('message', 'لا يوجد نص')
    
    # قالب إعلاني احترافي
    formatted_msg = (
        f"🔱 <b>Smart Deals Exclusive</b> 🔱\n\n"
        f"📢 {msg}\n\n"
        f"📍 طنجة، المغرب 🇲🇦\n"
        f"🔗 تابعنا: {CHANNEL_ID}"
    )
    
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {"chat_id": CHANNEL_ID, "text": formatted_msg, "parse_mode": "HTML"}
    res = requests.post(url, data=payload)
    return {"status": "success", "details": res.json()}

@app.route('/update_currency', methods=['GET'])
def update_currency():
    rate = 10.15 # سعر صرف تقريبي للدرهم 🇲🇦
    msg = f"💰 <b>تحديث العملة</b>\n\n💵 1 دولار = {rate} درهم مغربي\n\n🔱 Smart Deals"
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHANNEL_ID, "text": msg, "parse_mode": "HTML"})
    return {"status": "currency updated"}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
