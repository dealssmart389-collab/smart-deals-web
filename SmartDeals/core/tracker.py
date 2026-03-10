import time
import requests

def track():
    # هنا نضع منطق فحص الأسعار مستقبلاً
    print("🚀 رادار العروض يعمل الآن في خلفية Termux...")
    # إرسال تنبيه تجريبي
    requests.post("http://127.0.0.1:5000/send_ad", json={"message": "📢 تنبيه: تم رصد عرض جديد في سوق كازابلانكا!"})

if __name__ == "__main__":
    track()
