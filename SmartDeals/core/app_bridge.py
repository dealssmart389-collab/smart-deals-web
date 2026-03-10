from flask import Flask, request
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

# مفاتيح التحكم الخاصة بك
TOKEN = "REAL_TOKEN_HERE" 
CHAT_ID = "8389318428"

@app.route('/send_ad', methods=['POST'])
def send_ad():
    try:
        data = request.json
        message = data.get('message', 'إشعار من عالم العنان المتقدم 🚀')
        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
        payload = {"chat_id": CHAT_ID, "text": message, "parse_mode": "HTML"}
        
        response = requests.post(url, data=payload)
        return {"status": "success", "telegram_response": response.status_code}
    except Exception as e:
        return {"status": "error", "message": str(e)}, 500

if __name__ == '__main__':
    # التشغيل على جميع الواجهات لضمان تخطي عقبة الـ VPN
    app.run(host='0.0.0.0', port=5000)
