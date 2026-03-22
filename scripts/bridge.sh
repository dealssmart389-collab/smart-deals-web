#!/data/data/com.termux/files/usr/bin/bash

# تفعيل الترحيب السيادي
echo -e "\e[1;32m2026 سيادة نظام منير نشط الآن...\e[0m"

# وظيفة التحدث
function redmi_speak() {
    termux-tts-speak "$1"
}

# فحص البطارية
bat=$(termux-battery-status | grep percentage | cut -d: -f2 | tr -d ' ,')
echo "🔋 مستوى طاقة Redmi: $bat%"

# إرسال تقرير التشغيل للعقل
curl -s -X POST http://127.0.0.1:5000/think      -H "Content-Type: application/json"      -d "{\"query\": \"نظام السيادة بدأ بالعمل، البطارية $bat%\"}"

redmi_speak "تمت إعادة تشغيل الأنظمة السيادية سيدي منير."
