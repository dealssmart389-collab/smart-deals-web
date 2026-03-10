from flask import Flask, request
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

# 🔑 الإعدادات الأمنية - تأكد من وضع التوكن الخاص بك هنا
TOKEN = "7543829104:AAH_Example_Token" # استبدل بالتوكن الحقيقي
CHANNEL_ID = "@mSmartDeals_MA" # معرف القناة الرسمي

@app.route('/send_ad', methods=['POST'])
def send_ad():
    """إرسال إعلانات من واجهة التطبيق إلى القناة بتنسيق HTML"""
    try:
        data = request.json
        msg = data.get('message', 'لا يوجد نص')
        
        # قالب إعلاني احترافي مغربي 🔱
        formatted_msg = (
            f"🔱 <b>Smart Deals Exclusive</b> 🔱\n\n"
            f"📢 {msg}\n\n"
            f"📍 طنجة، المغرب 🇲🇦\n"
            f"🔗 تابعنا لأقوى العروض: {CHANNEL_ID}"
        )
        
        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
        payload = {
            "chat_id": CHANNEL_ID, 
            "text": formatted_msg, 
            "parse_mode": "HTML"
        }
        res = requests.post(url, data=payload)
        return {"status": "success", "response": res.json()}
    except Exception as e:
        return {"status": "error", "message": str(e)}

@app.route('/update_currency', methods=['GET'])
def update_currency():
    """تحديث سعر الصرف آلياً في القناة"""
    rate = 10.15 # سعر الدرهم الحالي 🇲🇦
    msg = (
        f"💰 <b>تحديث سعر الصرف اليومي</b>\n\n"
        f"💵 1 دولار = {rate} درهم مغربي 🇲🇦\n\n"
        f"🔱 Smart Deals"
    )
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    res = requests.post(url, data={
        "chat_id": CHANNEL_ID, 
        "text": msg, 
        "parse_mode": "HTML"
    })
    return {"status": "currency updated", "details": res.json()}

if __name__ == '__main__':
    # تشغيل السيرفر على المنفذ 5000
    app.run(host='0.0.0.0', port=5000)
