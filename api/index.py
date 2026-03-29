from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

TOKEN = "8713127522:AAGfj4acg204MMc0SX7keJNtP4fWN9L-lYQ"
CHAT_ID = "7984067238"

# تخزين مؤقت للإعدادات (في الذاكرة)
latest_config = {"image": "", "letter": "", "button": ""}

@app.route('/api/save', methods=['POST'])
def save_data():
    global latest_config
    data = request.json
    latest_config = data # تحديث الإعدادات
    
    # إرسال للبوت
    text = f"🚀 بيانات جديدة:\n{data}"
    requests.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage", json={"chat_id": CHAT_ID, "text": text})
    return jsonify({"status": "success"})

@app.route('/api/get', methods=['GET'])
def get_config():
    return jsonify(latest_config)

def handler(environ, start_response):
    return app(environ, start_response)
