import requests  # الأداة رقم 8 (تتخطى فشل التشفير)
import time

# مصفوفة الإعجاز الرياضي
matrix = {
    1: "C", 
    2: "AI", 
    3: "Pip", 
    4: "Nano", 
    5: "Clang", 
    6: "Python",
    8: "Requests",
    10: "Repository"
}

def validate_system():
    print("🧪 جاري فحص تناسق الأرقام والأدوات...")
    for num, tool in matrix.items():
        if len(tool) == num:
            print(f"✅ [رقم {num}] الأداة {tool} متوافقة حسابياً.")
        else:
            print(f"⚠️ [رقم {num}] تنبيه: خلل في التناسب.")

def connect_neural_core(prompt):
    # استخدام API مباشر لتخطي خطأ 'ModuleNotFoundError: No module named google'
    url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent"
    api_key = "ضع_مفتاحك_هنا" 
    
    headers = {'Content-Type': 'application/json'}
    data = {"contents": [{"parts":[{"text": prompt}]}]}
    
    print(f"\n📡 جاري الاتصال بالمركز العصبي لـ Smart Deals...")
    try:
        response = requests.post(f"{url}?key={api_key}", json=data, headers=headers)
        return response.json()['candidates'][0]['content']['parts'][0]['text']
    except Exception as e:
        return f"❌ خطأ في الاتصال (رقم 0): {e}"

if __name__ == "__main__":
    validate_system()
    # تجربة المركز العصبي
    print(connect_neural_core("قم بتحليل جاهزية مشروع Driving AI 2026"))
