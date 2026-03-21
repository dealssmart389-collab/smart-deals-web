async function askTimo() {
    const input = document.getElementById('user-input-field');
    const query = input.value.trim();
    if(!query) return;

    const log = document.getElementById('log-screen');
    log.innerHTML += `<div style="color: #888; margin-bottom: 5px;">👤 أنت: ${query}</div>`;
    
    // محاكاة التفكير العصبوني الفائق
    const typingId = "typing-" + Date.now();
    log.innerHTML += `<div id="${typingId}" style="color: var(--neon-green); opacity: 0.6;">> جاري سحب البيانات من السحابة العصبونية...</div>`;
    log.scrollTop = log.scrollHeight;

    try {
        // الربط مع واجهة برمجة تطبيقات ذكية (Gemini Engine)
        // ملاحظة: تيمو الآن يتكلم لغة العلم والسرعة
        const response = await fetch('https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key=YOUR_API_KEY', {
            method: 'POST',
            body: JSON.stringify({ contents: [{ parts: [{ text: "أجب كعالم خبير ومساعد ذكي جداً اسمه تيمو: " + query }] }] })
        });
        
        const data = await response.json();
        const aiText = data.candidates[0].content.parts[0].text;
        
        document.getElementById(typingId).remove();
        log.innerHTML += `<div style="color: var(--neon-green); border-right: 2px solid; padding-right:10px; margin: 10px 0;">🤖 تيمو (الروح الفائقة): ${aiText}</div>`;
        
    } catch (err) {
        document.getElementById(typingId).innerHTML = "> خطأ في الاتصال بالشبكة العصبونية. تأكد من مفتاح API.";
    }
    
    log.scrollTop = log.scrollHeight;
    input.value = "";
}
