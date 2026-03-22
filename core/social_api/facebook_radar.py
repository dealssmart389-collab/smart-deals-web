from facebook_scraper import get_posts
import json

def get_latest_fb_deal(page_id):
    """
    رادار فيسبوك لسحب آخر الصفقات المنشورة.
    page_id: اسم الصفحة أو رقمها التعريفي.
    """
    try:
        # ملاحظة: إذا كانت الصفحة عامة جداً قد لا تحتاج لكوكيز، 
        # ولكن يفضل استخدامه لتجنب الحظر.
        # نطلب آخر منشور واحد فقط (pages=1)
        for post in get_posts(page_id, pages=1):
            return {
                "text": post.get('post_text', 'No text')[:100] + "...",
                "url": post.get('post_url'),
                "image": post.get('image')
            }
    except Exception as e:
        # إذا حدث خطأ (مثل طلب تسجيل دخول)، سيعيد None
        print(f"Facebook Radar Log: {e}")
        return None

if __name__ == "__main__":
    # تجربة سريعة للرادار
    test_page = "اسم_صفحتك_هنا"
    deal = get_latest_fb_deal(test_page)
    if deal:
        print(f"✅ Success! Found: {deal['url']}")
    else:
        print("❌ Radar could not reach Facebook.")
