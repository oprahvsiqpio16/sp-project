from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# استبدل هذه القيم ببياناتك من BotFather و userinfobot
TOKEN = "8713127522:AAGfj4acg204MMc0SX7keJNtP4fWN9L-lYQ"
CHAT_ID = "7984067238"

@app.route('/api/save', methods=['POST'])
def save_data():
    try:
        data = request.json
        img = data.get('image')
        msg = data.get('letter')
        btn = data.get('button')

        # نص الرسالة التي ستصلك على تليجرام
        text = f"🚀 **تم إنشاء سكاما جديدة!**\n\n🖼️ الرابط: {img}\n📝 الخطاب: {msg}\n🔘 الزر: {btn}"
        
        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={text}&parse_mode=Markdown"
        requests.get(url)
        
        return jsonify({"status": "success"}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

def handler(environ, start_response):
    return app(environ, start_response)
