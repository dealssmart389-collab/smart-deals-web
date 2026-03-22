from core.database_manager import save_deal

def run_radar():
    print("📡 رادار بنلال يبحث عن عروض في TikTok و Instagram...")
    # محاكاة إيجاد عرض (بناءً على التوجيهات التي حددناها اليوم)
    deal_found = "تخفيض 50% على معدات ذكية"
    save_deal("TikTok @tvbenalal", deal_found)
    return {"status": "Online", "alerts": 1}

if __name__ == "__main__":
    run_radar()
