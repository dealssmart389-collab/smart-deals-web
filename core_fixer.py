import os, re

def final_polish():
    # استهداف الملفات الأساسية
    files = ['index.html', 'update.sh', 'evolve.sh']
    for file in files:
        if os.path.exists(file):
            with open(file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # 1. إصلاح شامل لتسلسلات الهروب (Escape Codes) لمنع SyntaxError
            content = content.replace('\\e[', '\033[').replace('\e[', '\033[')
            
            # 2. ترسيخ علامة BenalalAI في كل مكان
            content = content.replace('facebook', 'BenalalAI').replace('Facebook', 'BenalalAI')
            
            # 3. ترتيب السطور المبعثرة (Auto-Format)
            content = re.sub(r'\n\s*\n', '\n', content)
            
            with open(file, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✅ Robot: {file} is now Clean & Standardized.")

if __name__ == "__main__":
    final_polish()
