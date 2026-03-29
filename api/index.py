from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# بياناتك الخاصة التي زودتني بها
TOKEN = "8713127522:AAGfj4acg204MMc0SX7keJNtP4fWN9L-lYQ"
CHAT_ID = "7984067238"

@app.route('/api/save', methods=['POST'])
def save_data():
    try:
        data = request.json
        # استخراج البيانات من الخانات الثلاث في لوحة التحكم
        img_url = data.get('image', 'لم يتم إدخال رابط')
        letter_text = data.get('letter', 'لم يتم إدخال خطاب')
        button_text = data.get('button', 'لم يتم إدخال اسم للزر')

        # تنسيق الرسالة بشكل احترافي لتصلك كاملة
        full_message = (
            "🚀 **تم استقبال بيانات جديدة من اللوحة!**\n\n"
            f"🖼️ **رابط الصورة:**\n{img_url}\n\n"
            f"📝 **الخطاب (العنوان):**\n{letter_text}\n\n"
            f"🔘 **نص الزر:**\n{button_text}"
        )
        
        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
        payload = {
            "chat_id": CHAT_ID,
            "text": full_message,
            "parse_mode": "Markdown"
        }
        
        # إرسال الطلب إلى تليجرام
        response = requests.post(url, json=payload)
        
        if response.status_code == 200:
            return jsonify({"status": "success"}), 200
        else:
            return jsonify({"status": "error", "details": response.text}), 500

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

def handler(environ, start_response):
    return app(environ, start_response)
