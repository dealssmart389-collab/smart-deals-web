#!/bin/bash
# tremux
echo "🚀 Benalal AI: جاري دمج وتحديث النظام الموحد..."

# تشغيل الرادار لتحديث البيانات
python3 core/social_api/hybrid_radar.py

# إضافة جميع الملفات الجديدة (بما في ذلك README والواجهة)
git add .

# تسجيل التغيير بهوية المشروع
git commit -m "تحديث سيادي: دمج الرادارات الموحدة وتحديث واجهة Dashboard"

# الرفع النهائي
git push origin master

echo "✅ تم التوحيد بنجاح يا قائد منير! تفقد الرابط الآن."
