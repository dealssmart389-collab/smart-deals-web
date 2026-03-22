#!/bin/bash
echo "tremux"
echo "🚀 BenalalAI: Syncing Media & Code..."
# تشغيل مصلح الأكواد لضمان نظافة السطور
python3 core_fixer.py
# إضافة كافة الصور والفيديوهات الجديدة للمستودع
git add .
git commit -m "Upload: New Media from Mounir Phone"
git push origin main
echo "✅ Mission Accomplished, Mounir! Your media is now LIVE."
