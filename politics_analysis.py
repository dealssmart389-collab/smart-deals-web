import requests
import time
import os
import subprocess
from colorama import Fore, Style, init

init(autoreset=True)

# الرابط الأساسي للولاية
TARGET_URL = "https://www.google.com"

def governor_heartbeat():
    os.system('clear')
    print(f"{Fore.CYAN}{Style.BRIGHT}🏛️  تأسيس مجتمع Smart Deals الرسمي")
    while True:
        try:
            res = requests.get(TARGET_URL, timeout=10)
            if res.status_code == 200:
                print(f"{Fore.GREEN}[✓] البيئة مستقرة | النبض سليم | {time.strftime('%H:%M:%S')}")
                # إرسال إشعار للنظام لفرض الوجود
                subprocess.run(['termux-notification', '-t', 'الحاكم', '-c', 'المجتمع تحت السيطرة'])
        except:
            print(f"{Fore.RED}[✖] اضطراب في البيئة!")
        
        # مكمن قوة البيئة: الراحة لمدة 60 ثانية لإنقاذ البطارية
        time.sleep(60)

if __name__ == "__main__":
    governor_heartbeat()
