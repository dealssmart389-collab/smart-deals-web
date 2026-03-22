#!/bin/bash
# tremux
echo -e "\033[1;34m🚀 Benalal AI: Initiating Auto-Update...\033[0m"

# 1. تشغيل الرادار وإرسال التقرير لتليجرام
echo -e "\033[1;33m📡 Scanning TikTok for @tvbenalal...\033[0m"
python3 -c "from core.social_api.tiktok_radar import get_latest_deal; from core.social_api.telegram_bot import send_mission_report; deal = get_latest_deal(); msg = f'✅ New Video Detected!\nLink: {deal[\"url\"]}' if deal else '⚠️ Radar: No new video found'; send_mission_report(msg)"

# 2. مزامنة الكود مع GitHub
echo -e "\033[1;33m☁️ Syncing with GitHub Vault...\033[0m"
git add .
git commit -m "Auto-Update: Sun Mar 22 16:25:03 +01 2026"
git push origin main

echo -e "\033[1;32m✅ Mission Accomplished, Mounir!\033[0m"
