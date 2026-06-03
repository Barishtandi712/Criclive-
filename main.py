@app.route('/live')
def live_matches():
    try:
        link = "https://www.cricbuzz.com/cricket-match/live-scores"

        headers = {
            "User-Agent": "Mozilla/5.0"
        }

        response = requests.get(link, headers=headers, timeout=10)
        response.raise_for_status()

        page = BeautifulSoup(response.text, "lxml")

        container = page.find(
            "div",
            class_="cb-col cb-col-100 cb-bg-white"
        )

        if not container:
            return jsonify({
                "status": "error",
                "message": "Cricbuzz page structure changed"
            }), 500

        matches = container.find_all(
            "div",
            class_="cb-scr-wll-chvrn cb-lv-scrs-col"
        )

        live_matches = []

        for match in matches:
            live_matches.append(match.get_text(" ", strip=True))

        return jsonify({
            "status": "success",
            "count": len(live_matches),
            "matches": live_matches
        })

    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500
