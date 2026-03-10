from flask import Flask, request, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

# إعدادات البوت والقناة
TOKEN = "8654310950:AAFdC6w93szpM-C5Vgtv5lM4D-u-zFkLyIM"
CHANNEL_ID = "@mSmartDeals_MA"

@app.route('/update_currency', methods=['GET'])
def update_currency():
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {
        "chat_id": CHANNEL_ID,
        "text": "📊 <b>تحديث العملة</b>\n\n💰 1 دولار = 10.15 درهم",
        "parse_mode": "HTML"
    }
    response = requests.post(url, json=payload)
    return response.json()

@app.route('/send_deal', methods=['POST'])
def send_deal():
    data = request.json
    message = data.get('message', 'لا يوجد محتوى')
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {"chat_id": CHANNEL_ID, "text": message, "parse_mode": "HTML"}
    response = requests.post(url, json=payload)
    return response.json()

@app.route('/fetch_ali_details', methods=['POST'])
def fetch_ali_details():
    try:
        data = request.json
        product_url = data.get('url')
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
        response = requests.get(product_url, headers=headers, timeout=10)
        
        # استخدام html.parser لأنه مدمج ولا يحتاج تثبيت إضافي
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # جلب البيانات من Meta Tags لضمان الدقة
        title_tag = soup.find("meta", property="og:title")
        image_tag = soup.find("meta", property="og:image")
        
        title = title_tag["content"] if title_tag else "AliExpress Product"
        image = image_tag["content"] if image_tag else ""
        
        return jsonify({
            "ok": True,
            "title": title,
            "image": image,
            "url": product_url
        })
    except Exception as e:
        return jsonify({"ok": False, "error": str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
