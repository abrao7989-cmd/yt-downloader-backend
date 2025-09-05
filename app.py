from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

# Load API key from environment variable
RAPIDAPI_KEY = os.environ.get("RAPIDAPI_KEY")

@app.route("/")
def home():
    return {"status": "ok", "message": "YT Downloader Backend is running"}

@app.route("/download", methods=["GET"])
def download():
    video_url = request.args.get("url")
    format_type = request.args.get("format", "mp4")

    if not video_url:
        return jsonify({"error": "Missing url parameter"}), 400

    try:
        url = "https://instagram-tiktok-youtube-downloader.p.rapidapi.com/get-info"
        querystring = {"url": video_url}

        headers = {
            "x-rapidapi-host": "instagram-tiktok-youtube-downloader.p.rapidapi.com",
            "x-rapidapi-key": RAPIDAPI_KEY
        }

        response = requests.get(url, headers=headers, params=querystring)
        data = response.json()

        return jsonify({"status": "success", "data": data})

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
