import os
from core.social_api.telegram_bot import send_mission_report

def global_sync():
    print("\033[1;34m📡 Connecting to Global Network...\033[0m")
    
    # تنفيذ الرفع لـ GitHub
    os.system("git add .")
    os.system('git commit -m "Engine v2.0: Global Sync Verified"')
    result = os.system("git push origin main")
    
    if result == 0:
        msg = "🚀 Mission Accomplished: Code Secured on GitHub!"
        send_mission_report(msg)
        return f"\033[1;32m{msg}\033[0m"
    else:
        return "\033[1;31m❌ Sync Failed: Connection Error.\033[0m"
