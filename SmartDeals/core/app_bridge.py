import requests
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

TOKEN = "8654310950:AAFqsBQdlt3lEUA3F-ULm2kFj1s_B56sfic"
CHANNEL_ID = "@mSmartDeals_MA"

@app.route('/update_currency', methods=['GET'])
def update_currency():
    try:
        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
        payload = {
            "chat_id": CHANNEL_ID,
            "text": "💰 <b>تحديث العملة</b>\n💵 1 دولار = 10.15 درهم",
            "parse_mode": "HTML"
        }
        res = requests.post(url, json=payload, timeout=10)
        return jsonify(res.json())
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
