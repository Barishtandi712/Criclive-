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

page = BeautifulSoup(response.text, "html.parser")

return jsonify({
    "status": "success",
    "html_length": len(response.text)
})
        
except Exception as e:
    return jsonify({
            "error": str(e)
        }), 500
