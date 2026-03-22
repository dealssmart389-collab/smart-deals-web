import os
import google.generativeai as genai
from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import requests

# تحميل المفاتيح من ملف .env
load_dotenv()

app = Flask(__name__)
CORS(app)

# 1. إعداد ذكاء Gemini (العقل)
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel('gemini-1.5-flash')

# 2. وظيفة إرسال التنبيهات لتليجرام (الحارس)
def send_to_telegram(message):
    token = os.getenv('TELEGRAM_TOKEN')
    chat_id = os.getenv('TELEGRAM_CHAT_ID')
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {"chat_id": chat_id, "text": message, "parse_mode": "Markdown"}
    try:
        # إضافة timeout لضمان عدم تعليق السيرفر
        requests.post(url, data=payload, timeout=5)
    except Exception as e:
        print(f"❌ خطأ في إرسال التنبيه: {e}")

@app.route('/ask_timo', methods=['POST'])
def ask_timo():
    data = request.json
    query = data.get('query', '')
    
    # تعريف شخصية تيمو السيادية
    system_prompt = "أنت تيمو، المساعد الذكي لمنظومة Benalal AI 2026. صانعك هو منير بن علال. أجب بذكاء واحترافية."
    
    try:
        # توليد الإجابة باستخدام الذكاء الاصطناعي
        response = model.generate_content(f"{system_prompt}\nالسؤال: {query}")
        answer = response.text
        
        # إرسال تقرير لمنير على تليجرام
        report_msg = f"🛡️ *تنبيه Benalal AI*\n👤 المستخدم سأل: {query}\n🤖 رد تيمو: {answer[:100]}..."
        send_to_telegram(report_msg)
        
        return jsonify({"answer": answer})
    except Exception as e:
        return jsonify({"answer": "عذراً يا سيد منير، العقل الخارجي يحتاج إعادة اتصال."}), 500

if __name__ == '__main__':
    # التشغيل على localhost للأمان الرقمي
    print("🚀 Benalal AI Sentinel is Active...")
    app.run(host='127.0.0.1', port=5000)
