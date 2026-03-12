
import google.generativeai as genai

# إعداد المفتاح
genai.configure(api_key="YOUR_API_KEY")

def analyze_deal(price, description):
    print(f"تحليل الصفقة: {description} بسعر {price}")

analyze_deal("100 DH", "هاتف ذكي مستعمل بحالة جيدة")
