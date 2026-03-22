import os
import subprocess

def speak_alert(message):
    print(f"🔊 نظام بنلال ينطق: {message}")
    # استخدام أمر termux-tts-speak للنطق بالعربية
    subprocess.run(['termux-tts-speak', '-l', 'ar', message])

def check_and_announce(radar_results):
    # إذا وجد الرادار صفقات أو تحديثات جديدة
    if radar_results.get('alerts', 0) > 0:
        msg = f"قائد منير، تم رصد {radar_results['alerts']} صفقات جديدة على الرادار"
        speak_alert(msg)
    else:
        # تنبيه دوري بأن النظام يعمل
        speak_alert("نظام بنلال للذكاء الاصطناعي في وضع الاستعداد")

if __name__ == "__main__":
    # تجربة النظام الصوتي الآن
    check_and_announce({'alerts': 1})
