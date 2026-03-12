from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/alerts')
def get_alerts():
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            'Referer': 'https://www.oref.org.il/',
            'X-Requested-With': 'XMLHttpRequest'
        }
        r = requests.get(
            'https://www.oref.org.il/WarningMessages/History/AlertsHistory.json',
            headers=headers,
            timeout=10
        )
        data = r.json()
        return jsonify(data[:20] if data else [])
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/')
def home():
    return "Oref Proxy OK"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
