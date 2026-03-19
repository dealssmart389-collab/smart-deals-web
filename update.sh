#!/data/data/com.termux/files/usr/bin/bash
echo "tremux"
echo "🌀 جاري تفعيل بروتوكول الجبروت الرقمي..."

# تحديث الكود وتطويره آلياً قبل الرفع
python3 ~/SmartDeals/evolve.sh 

cd ~/SmartDeals
git add .
git commit -m "System Evolution: $(date)"
git push origin main --force

echo "🔱 تم إخضاع الواقع.. الموقع حي الآن بملايين الأعمدة."
