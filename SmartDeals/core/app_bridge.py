@app.route('/send_ad', methods=['POST'])
def send_ad():
    data = request.json
    msg = data.get('message', '')
    
    # قالب إعلاني مغربي احترافي 🔱
    formatted_msg = (
        f"🔱 <b>Smart Deals Exclusive</b> 🔱\n\n"
        f"📢 {msg}\n\n"
        f"📍 طنجة، المغرب 🇲🇦\n"
        f"🔗 تابعنا لأقوى العروض: @mSmartDeals_MA"
    )
    
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {
        "chat_id": "@mSmartDeals_MA", # المعرف الجديد
        "text": formatted_msg,
        "parse_mode": "HTML"
    }
    res = requests.post(url, data=payload)
    return {"status": "success", "response": res.json()}
