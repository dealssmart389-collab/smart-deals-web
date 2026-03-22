import os
from core.social_api.telegram_bot import send_mission_report
from core.social_api.tiktok_radar import get_latest_deal

def main_menu():
    print("\033[1;32mWelcome back, Commander Mounir!!\033[0m")
    print("========================================")
    print("         BENALAL AI CORE v2.5")
    print("========================================")
    print("1. Add Product      (إضافة منتج)")
    print("2. Show Vault       (عرض المخزن)")
    print("3. Mission Push     (🚀 الرفع للعالم)")
    print("4. Radar Scan       (📡 رادار تيك توك)")
    print("5. Exit             (خروج)")
    
    choice = input("\033[1;33mMounir >> \033[0m")
    
    if choice == '3':
        os.system("git add . && git commit -m 'Sync' && git push origin main")
        send_mission_report("GitHub Sync Completed Successfully!")
    elif choice == '4':
        print("\033[1;34m🔎 Scanning @tvbenalal for new deals...\033[0m")
        deal = get_latest_deal()
        if deal:
            report = f"🎥 New Deal Found!\nTitle: {deal['title']}\nURL: {deal['url']}"
            send_mission_report(report)
            print(f"\033[1;32m✅ Deal reported to Telegram!\033[0m")
        else:
            print("\033[1;31m❌ No new deals found.\033[0m")
    elif choice == '5':
        exit()

if __name__ == "__main__":
    while True:
        main_menu()
