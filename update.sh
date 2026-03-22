#!/bin/bash
# tremux
echo "🚀 Benalal AI: جاري دمج وتحديث النظام الموحد..."

# محاولة تشغيل الرادار (سيتم تخطي الخطأ إذا استمرت مشكلة المكتبات)
python3 core/social_api/hybrid_radar.py || echo "⚠️ تنبيه: الرادار يحتاج لتثبيت lxml_html_clean"

# العمليات الأساسية لـ Git
git add .
git commit -m "تحديث سيادي المجلدات والملفات الموحدة"

# محاولة الرفع للفرع المتاح
git push origin master || git push origin main

echo "✅ تم التوحيد النهائي يا قائد منير!"
