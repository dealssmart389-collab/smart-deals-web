import requests

def scan_market(keyword):
    print(f"🔎 Benalal AI Core is scanning for: {keyword}...")
    # هنا سنضع روابط الـ API الخاصة بـ Jumia أو AliExpress لاحقاً
    # حالياً سنقوم بمحاكاة جلب البيانات لتجهيز القاعدة
    results = [
        {"name": "Smart Watch V8", "price": "199 DH", "trend": "High"},
        {"name": "Wireless Pods Pro", "price": "250 DH", "trend": "Viral"}
    ]
    for item in results:
        print(f"✅ Found: {item['name']} | Price: {item['price']} | Status: {item['trend']}")

if __name__ == "__main__":
    scan_market("Electronics")
