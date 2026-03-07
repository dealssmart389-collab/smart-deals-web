#!/data/data/com.termux/files/usr/bin/bash

echo "--- بدء عملية التحديث والتنظيف لزيادة السرعة ---"

# تحديث المستودعات والحزم
pkg update -y && pkg upgrade -y

# تنظيف الكاش والملفات غير الضرورية
pkg clean
pkg autoclean

# حذف ملفات التخزين المؤقت
rm -rf ~/.cache/*

echo "--- تم التنظيف بنجاح، الهاتف الآن أخف! ---"
