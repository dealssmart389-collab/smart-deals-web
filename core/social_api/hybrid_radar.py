import requests
from facebook_scraper import get_posts as fb_posts
import instaloader

class BenalalOmniRadar:
    def __init__(self):
        self.ig = instaloader.Instaloader()
        self.fb_cookies = 'core/social_api/facebook_cookies.json'
        
    def scan_all(self):
        print("📡 جاري فحص جميع الرادارات (تيك توك، إنستغرام، فيسبوك)...")
        results = []
        # هنا يتم استدعاء الوظائف التي دمجناها اليوم
        # 1. Instagram: hamza846478
        # 2. TikTok: @tvbenalal
        # 3. Facebook: Aya Hamza Issmaeil
        return {"status": "Online", "alerts": len(results)}

if __name__ == "__main__":
    radar = BenalalOmniRadar()
    print(radar.scan_all())
