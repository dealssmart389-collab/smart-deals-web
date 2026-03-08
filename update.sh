#!/data/data/com.termux/files/usr/bin/bash

# 🚀 Smart Deals - Auto Pilot Update System V2.1
echo "🔄 جاري بدء تحديث المتجر الذكي..."

# 1. التأكد من حماية الملفات الحساسة (الدرع الأمني)
if [ ! -f .gitignore ]; then
    echo ".ssh/" > .gitignore
    echo "*.zip" >> .gitignore
    echo "*.ab" >> .gitignore
    echo "storage/" >> .gitignore
    echo "✅ تم إنشاء درع الحماية بنجاح."
fi

# 2. إضافة التعديلات الجديدة (ذكاء Gemini)
git add .

# 3. توثيق التحديث مع التوقيت
current_time=$(date "+%Y-%m-%d %H:%M")
git commit -m "تحديث تلقائي للمتجر الذكي: $current_time 🚀"

# 4. الرفع القوي والمؤمن إلى GitHub
echo "📤 جاري رفع البيانات إلى السحابة..."
git push -f origin main

echo "✨ مبروك! متجرك الآن محدث وبأعلى معايير الأمان."
