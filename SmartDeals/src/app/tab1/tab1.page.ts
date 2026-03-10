sendTelegramAd() {
  // الرابط المحلي الذي يربط التطبيق بالجسر في تيرمكس
  const url = "http://localhost:5000/send_ad";

  if (!this.adMessage || this.adMessage.trim() === "") {
    alert("⚠️ من فضلك اكتب نص الإعلان أولاً");
    return;
  }

  fetch(url, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ message: this.adMessage })
  })
  .then(res => res.json())
  .then(data => {
    if (data.status === "success") {
      alert("✅ تم بنجاح! الإعلان الآن في القناة");
      this.adMessage = ""; // مسح النص بعد الإرسال الناجح
    } else {
      alert("❌ عذراً: " + (data.details?.description || "فشل الربط"));
    }
  })
  .catch(err => {
    console.error(err);
    alert("⚠️ خطأ في الاتصال: تأكد أن الجسر يعمل في Termux");
  });
}
