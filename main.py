from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/alerts')
def get_alerts():
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Referer': 'https://www.oref.org.il/',
            'X-Requested-With': 'XMLHttpRequest',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Language': 'he-IL,he;q=0.9',
        }
        r = requests.get(
            'https://www.oref.org.il/WarningMessages/History/AlertsHistory.json',
            headers=headers,
            timeout=10
        )
        text = r.text.strip()
        if not text or text == 'null':
            return jsonify([])
        data = r.json()
        return jsonify(data[:20] if data else [])
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/')
def home():
    return "Oref Proxy OK"

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)
