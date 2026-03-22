#!/bin/bash
echo "tremux"
echo "🚀 BenalalAI: Initiating Auto-Fix & Update..."
# تشغيل الروبوت المصلح أولاً لتنظيف الكود
python3 core_fixer.py
# رفع التحديثات النظيفة لـ GitHub
git add .
git commit -m "System Evolution: BenalalAI Identity & Auto-Fixer"
git push origin main
echo "✅ Mission Accomplished, Mounir!"
