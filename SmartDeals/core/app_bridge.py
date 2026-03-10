from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# الإعدادات الأساسية التي تعمل بنجاح
TOKEN = "8654310950:AAFdC6w93szpM-C5Vgtv5lM4D-u-zFkLyIM"
CHANNEL_ID = "@mSmartDeals_MA"

@app.route('/update_currency', methods=['GET'])
def update_currency():
    try:
        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
        payload = {
            "chat_id": CHANNEL_ID,
            "text": "📊 <b>تحديث العملة</b>\n\n💰 1 دولار = 10.15 درهم",
            "parse_mode": "HTML"
        }
        response = requests.post(url, json=payload)
        return response.json()
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

# المسار الجديد الذي سيحل مشكلة الـ 404
@app.route('/send_deal', methods=['POST'])
def send_deal():
    try:
        data = request.json
        message = data.get('message', 'لا يوجد محتوى للرسالة')
        
        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
        payload = {
            "chat_id": CHANNEL_ID,
            "text": message,
            "parse_mode": "HTML"
        }
        response = requests.post(url, json=payload)
        return response.json()
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
