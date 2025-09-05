from flask import Flask, request, jsonify
from flask_cors import CORS
import os, requests

app = Flask(__name__)
CORS(app)  # Enable cross-origin requests

# Load API key
RAPIDAPI_KEY = os.environ.get("RAPIDAPI_KEY")

@app.route("/", methods=["GET"])
def home():
    return {"status": "ok", "message": "YT Downloader Backend is running"}

@app.route("/download", methods=["POST"])
def download():
    try:
        body = request.get_json()
        video_url = body.get("url")
        format_type = body.get("format", "mp4")

        if not video_url:
            return jsonify({"error": "Missing url parameter"}), 400

        url = "https://instagram-tiktok-youtube-downloader.p.rapidapi.com/get-info"
        querystring = {"url": video_url, "format": format_type}

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
