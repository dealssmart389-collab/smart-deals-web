from flask import Flask, request
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

TOKEN = "ضع_التوكن_الحقيقي_هنا" # استبدل هذا بتوكن BotFather الحقيقي
CHAT_ID = "8389318428"

@app.route('/send_ad', methods=['POST'])
def send_ad():
    try:
        data = request.json
        msg = data.get('message', 'نبض من عالم العنان!')
        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
        res = requests.post(url, data={"chat_id": CHAT_ID, "text": msg})
        return {"status": "success", "code": res.status_code}
    except Exception as e:
        return {"status": "error", "msg": str(e)}, 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
