# اسم الملف: gatekeeper.py
from flask import Flask
import politics_analysis as auditor

app = Flask(__name__)

@app.route('/notify_payment_access')
def notify():
    # استدعاء التنبيه المحصن الذي فحصناه بـ Bandit
    auditor.send_secure_notification("تنبيه NEURAL PAY", "هناك محاولة دخول جديدة لصفحة الدفع!")
    return "Notification Sent", 200

if __name__ == "__main__":
    app.run(port=5000)
