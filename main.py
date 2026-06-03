from flask import Flask, jsonify
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "status": "running"
    })

@app.route('/live')
def live_matches():
    try:
        link = "https://www.cricbuzz.com/cricket-match/live-scores"

        headers = {
            "User-Agent": "Mozilla/5.0"
        }

        response = requests.get(link, headers=headers, timeout=10)

        return jsonify({
            "status": "success"
        })

    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 500
