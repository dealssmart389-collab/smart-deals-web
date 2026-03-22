import google.generativeai as genai
import os

def analyze_product_image(image_path):
    # إعداد المفتاح (سنقوم بضبطه لاحقاً)
    api_key = os.getenv("GEMINI_API_KEY")
    genai.configure(api_key=api_key)
    
    model = genai.GenerativeModel('gemini-1.5-flash')
    
    # محاكاة تحليل الصورة في حالة عدم وجود مفتاح حالياً
    print(f"📸 Benalal Eye is scanning: {image_path}")
    return "منتج ذكي عالي الجودة - مقترح للبيع بـ 300 درهم"

if __name__ == "__main__":
    # تجربة فحص سريعة
    print(analyze_product_image("sample.jpg"))
EOF# tremux
python Benalal_AI_Core.py
mkdir -p core/database core/ai_logic core/inventory
export GEMINI_API_KEY='YOUR_KEY
mkdir -p core/database core/ai_logic core/inventory


# tremux
cat <<EOF > Benalal_AI_Core.py
import os
import time

def clear():
    os.system('clear')

def main_menu():
    # الألوان الملكية: أسود، ذهبي، أخضر، أزرق
    GOLD = '\033[1;33m'
    GREEN = '\033[1;32m'
    BLUE = '\033[1;34m'
    WHITE = '\033[1;37m'
    RESET = '\033[0m'
    
    while True:
        clear()
        print(f"{BLUE}========================================{RESET}")
        print(f"{GOLD}          BENALAL AI CORE v1.0          {RESET}")
        print(f"{BLUE}========================================{RESET}")
        print(f"{GREEN}[✔] System: Online    | [✔] Storage: Locked{RESET}")
        print(f"{GREEN}[✔] Android: 15       | [✔] API: 35{RESET}")
        print(f"{BLUE}----------------------------------------{RESET}")
        print(f"{WHITE}1. Add New Product     (إضافة منتج جديد){RESET}")
        print(f"{WHITE}2. Start Vision Eye    (تفعيل العين الرقمية){RESET}")
        print(f"{WHITE}3. Show All Inventory  (عرض المخزن الأبدي){RESET}")
        print(f"{WHITE}4. Exit System         (إغلاق النظام){RESET}")
        print(f"{BLUE}----------------------------------------{RESET}")
        
        choice = input(f"{GOLD}Mounir >> {RESET}")
        
        if choice == '1':
            print(f"{GREEN}Opening Storage...{RESET}")
            time.sleep(1)
        elif choice == '2':
            print(f"{GOLD}Activating Vision AI...{RESET}")
            time.sleep(1)
        elif choice == '3':
            print(f"{BLUE}Retrieving Data...{RESET}")
            time.sleep(1)
        elif choice == '4':
            print(f"{GOLD}Shutting down Benalal Core...{RESET}")
            break
        else:
            print("Invalid Option!")
            time.sleep(1)

if __name__ == "__main__":
    main_menu()
