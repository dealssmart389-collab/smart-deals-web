@app.route('/update_currency', methods=['GET'])
def update_currency():
    # في النسخة المتقدمة سنستخدم API حقيقي، هنا نضع السعر التقريبي
    rate = 10.15 
    msg = f"💰 <b>تحديث سعر الصرف اليومي</b>\n\n💵 1 دولار = {rate} درهم مغربي 🇲🇦\n\n<i>تم التحديث تلقائياً بواسطة Smart Deals 🔱</i>"
    
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": "@mSmartDeals_MA", "text": msg, "parse_mode": "HTML"})
    return {"status": "currency updated"}
