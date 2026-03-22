import instaloader
from facebook_scraper import get_posts

def scan_meta_deals():
    # رادار إنستغرام
    L = instaloader.Instaloader()
    try:
        profile = instaloader.Profile.from_username(L.context, "YOUR_INSTA_USERNAME")
        latest_post = next(profile.get_posts())
        insta_url = f"https://www.instagram.com/p/{latest_post.shortcode}/"
    except:
        insta_url = None

    return {"instagram": insta_url}
