from flask import Flask, jsonify
from bs4 import BeautifulSoup
import requests
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

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

        response = requests.get(
            link,
            headers=headers,
            timeout=20
        )
        response.raise_for_status()

        page = BeautifulSoup(response.text, "html.parser")

        matches = []

        for match in page.find_all("div", class_="cb-mtch-lst"):
            matches.append(match.get_text(" ", strip=True))

        return jsonify({
            "status": "success",
            "matches": matches
        })

    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 500
