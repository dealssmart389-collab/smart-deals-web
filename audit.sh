#!/bin/bash
echo -e "[1;34m[*] جاري مراجعة ملفات Smart Deals...[0m"

echo -e "
[1;33m[1] فحص ملفات HTML:[0m"
tidy -e index.html

echo -e "
[1;33m[2] فحص أمان كود Python (إن وجد):[0m"
bandit -r .

echo -e "
[1;33m[3] فحص أخطاء كود Javascript:[0m"
# سنفحص كل ملفات .js في المجلد
find . -name "*.js" -exec npx eslint {} +

echo -e "
[1;32m[✓] انتهت المراجعة التحليلية.[0m"