from flask import Flask, request, jsonify
from flask_cors import CORS
import subprocess

app = Flask(__name__)
CORS(app)

@app.route('/exec', methods=['POST'])
def execute():
    command = request.json.get('command')
    try:
        # تنفيذ الأمر وجلب النتيجة
        result = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
        return jsonify({"status": "success", "output": result.decode('utf-8')})
    except Exception as e:
        return jsonify({"status": "error", "output": str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
