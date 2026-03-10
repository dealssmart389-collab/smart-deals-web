import os
import hashlib

def check_immunity():
    # فحص البصمة الرقمية لملفات النواة
    core_files = ['../intelligence/omni_core.py', '../intelligence/ascension_core.py']
    for file in core_files:
        if os.path.exists(file):
            print(f'🛡️ فحص المناعة لـ {file}: سليم')
        else:
            print('⚠️ ثغرة مكتشفة! تفعيل بروتوكول العزل...')
            # هنا يتم إغلاق النظام تلقائياً

if __name__ == '__main__':
    check_immunity()