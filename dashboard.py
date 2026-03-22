import os

def launch():
    # الألوان الملكية
    GOLD = '\033[1;33m'
    GREEN = '\033[1;32m'
    BLUE = '\033[1;34m'
    BLACK_BG = '\033[40m'
    RESET = '\033[0m'

    os.system('clear')
    print(f"{BLACK_BG}{GOLD}========================================{RESET}")
    print(f"{BLACK_BG}{GOLD}      SMART DEALS CONTROL CENTER        {RESET}")
    print(f"{BLACK_BG}{GOLD}========================================{RESET}")
    print(f"{BLACK_BG}{GREEN}[+] Status: ONLINE (Android 15 / API 35){RESET}")
    print(f"{BLACK_BG}{BLUE}[+] AI Engine: Gemini Active{RESET}")
    print(f"{BLACK_BG}{GOLD}[+] Theme: Dark Obsidian & Gold{RESET}")
    print(f"{BLACK_BG}{GOLD}----------------------------------------{RESET}")
    print(f"{BLACK_BG}{GREEN}[1] الحساب (Profile){RESET}")
    print(f"{BLACK_BG}{GOLD}[2] الإعدادات (Settings){RESET}")
    print(f"{BLACK_BG}{BLUE}[3] المخازن (Inventory){RESET}")
    print(f"{BLACK_BG}{GOLD}========================================{RESET}")

if __name__ == "__main__":
    launch()
