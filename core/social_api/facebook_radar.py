import requests

def get_latest_fb_deal():
    # الصق التوكن الذي استخرجناه من صفحة المطورين هنا
    token = "EA...ضع_التوكن_هنا"
    # معرف الحساب أو الصفحة
    page_id = "Aya.Hamza.Issmaeil" 
    
    url = f"https://graph.facebook.com/v19.0/{page_id}/posts?access_token={token}&limit=1"
    
    try:
        r = requests.get(url).json()
        if 'data' in r and len(r['data']) > 0:
            latest_post = r['data'][0]
            return {
                "message": latest_post.get('message', 'New Update from Aya'),
                "url": f"https://facebook.com/{latest_post['id']}"
            }
    except Exception as e:
        print(f"Error: {e}")
        return None
