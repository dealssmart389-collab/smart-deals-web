import os
import re

def fix_script_errors(file_path):
    if not os.path.exists(file_path):
        return
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. إصلاح خطأ تسلسل الهروب المشهور في الصور الخاصة بك (Escape Sequence)
    # يحول \e إلى \033 ليفهمها تيرموكس بشكل صحيح
    fixed_content = content.replace('\\e[', '\033[').replace('\e[', '\033[')
    
    # 2. ترتيب السطور وإزالة الفراغات المزدوجة المزعجة
    fixed_content = re.sub(r'\n\s*\n', '\n', fixed_content)
    
    # 3. محاولة إصلاح الأخطاء النصية في الـ HTML (إغلاق التاجات المفتوحة)
    if file_path.endswith('.html'):
        if '</body>' not in fixed_content:
            fixed_content += '\n</body>\n</html>'

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(fixed_content)
    print(f"✅ تم إصلاح وترتيب: {file_path}")

# قائمة الملفات التي ظهرت فيها المشاكل في صورك
files_to_fix = ['evolve.sh', 'index.html', 'update.sh']

for file in files_to_fix:
    fix_script_errors(file)

print("\n🚀 الروبوت انتهى! تم تنظيف الأكواد بنجاح.")
