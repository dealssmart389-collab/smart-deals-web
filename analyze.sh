#!/bin/bash
echo -e "[1;34m[*] جاري تشغيل المختبر الذكي لـ Smart Deals...[0m"

# 1. فحص أمان كود البايثون (البحث عن ثغرات)
echo -e "
[1;33m[!] فحص الأمان (Bandit):[0m"
bandit -r .

# 2. فحص جودة الكود (Flake8)
echo -e "
[1;33m[!] فحص جودة الكود التقني:[0m"
flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics

# 3. فحص ملفات الويب
echo -e "
[1;32m[✓] مراجعة البيئة اكتملت.[0m"