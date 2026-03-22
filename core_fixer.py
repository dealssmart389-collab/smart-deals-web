import os, re

def clean_and_format():
    files = ['index.html', 'evolve.sh', 'update.sh']
    for file in files:
        if os.path.exists(file):
            with open(file, 'r', encoding='utf-8') as f:
                content = f.read()
            # تصحيح أخطاء الهروب التي ظهرت في الصور (Escape Sequence)
            content = content.replace('\\e[', '\033[').replace('\e[', '\033[')
            # ترتيب السطور وحذف الفراغات المزدوجة
            content = re.sub(r'\n\s*\n', '\n', content)
            # استبدال العلامات التجارية بهوية BenalalAI
            content = content.replace('facebook', 'BenalalAI').replace('الفايسبوك', 'BenalalAI')
            with open(file, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✅ Robot: Fixed and Formatted {file}")

if __name__ == "__main__":
    clean_and_format()
