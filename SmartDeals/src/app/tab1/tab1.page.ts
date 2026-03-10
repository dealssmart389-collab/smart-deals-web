adMessage: string = "";

sendTelegramAd() {
  const url = "http://localhost:5000/send_ad";
  fetch(url, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ message: this.adMessage })
  })
  .then(res => res.json())
  .then(data => alert("تم الإرسال لتيليجرام بنجاح! 🚀"))
  .catch(err => alert("خطأ: تأكد أن سيرفر تيرمكس يعمل!"));
}
