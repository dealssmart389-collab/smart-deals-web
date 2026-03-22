import tweepy

def publish_to_x(message):
    # ستحتاج لإدخال مفاتيح API الخاصة بك من developer.x.com
    auth = tweepy.OAuthHandler("API_KEY", "API_SECRET")
    auth.set_access_token("ACCESS_TOKEN", "ACCESS_TOKEN_SECRET")
    api = tweepy.API(auth)
    
    try:
        api.update_status(message)
        return True
    except:
        return False
