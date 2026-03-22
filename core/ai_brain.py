import google.generativeai as genai
from flask import Flask, request, jsonify

# إعداد الهوية السيادية
genai.configure(api_key="YOUR_API_KEY")
model = genai.GenerativeModel('gemini-1.5-flash')
app = Flask(__name__)

@app.route('/think', methods=['POST'])
def think():
    try:
        query = request.json.get('query', '')
        response = model.generate_content(f"أنت ذكاء Redmi السيادي لمنير: {query}")
        return jsonify({"status": "success", "reply": response.text})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
