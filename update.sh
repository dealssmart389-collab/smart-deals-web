#!/bin/bash
# tremux
echo "🚀 Benalal AI: جاري تشغيل نظام اليقظة الصوتية..."

# تشغيل الرادار
python3 core/social_api/hybrid_radar.py

# تشغيل التنبيه الصوتي
python3 core/social_api/voice_alerts.py

# عمليات المزامنة مع GitHub باستخدام SSH
git add .
git commit -m "تحديث سيادي: تفعيل نظام التنبيهات الصوتية"
git push origin master

echo "✅ تم التحديث والنطق بنجاح يا قائد منير!"
