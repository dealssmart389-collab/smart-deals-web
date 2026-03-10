from flask import Flask, request
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

# 🔑 البيانات الحقيقية للربط
TOKEN = "YOUR_BOT_TOKEN_HERE" 
CHANNEL_ID = "@mSmartDeals_MA"

@app.route('/send_ad', methods=['POST'])
def send_ad():
    try:
        data = request.json
        msg = data.get('message', '')
        
        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
        payload = {
            "chat_id": CHANNEL_ID,
            "text": msg,
            "parse_mode": "HTML"
        }
        res = requests.post(url, data=payload)
        return {"status": "success", "details": res.json()}
    except Exception as e:
        return {"status": "error", "message": str(e)}

@app.route('/update_currency', methods=['GET'])
def update_currency():
    rate = 10.15 #
    msg = f"💰 <b>تحديث العملة</b>\n💵 1 دولار = {rate} درهم مغربي 🇲🇦"
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHANNEL_ID, "text": msg, "parse_mode": "HTML"})
    return {"status": "currency updated"}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
