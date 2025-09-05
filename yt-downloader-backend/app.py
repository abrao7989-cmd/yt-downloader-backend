from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

RAPIDAPI_KEY = "your-rapidapi-key"  # Replace with your actual key
RAPIDAPI_HOST = "instagram-tiktok-youtube-downloader.p.rapidapi.com"

@app.route("/download", methods=["GET"])
def download():
    url = request.args.get("url")
    format_type = request.args.get("format", "mp4")  # mp4, mp3, etc.

    if not url:
        return jsonify({"error": "URL is required"}), 400

    api_url = f"https://{RAPIDAPI_HOST}/get-info?url={url}"

    headers = {
        "x-rapidapi-host": RAPIDAPI_HOST,
        "x-rapidapi-key": RAPIDAPI_KEY
    }

    response = requests.get(api_url, headers=headers)
    if response.status_code != 200:
        return jsonify({"error": "Failed to fetch from API"}), 500

    data = response.json()
    return jsonify({"requested_format": format_type, "data": data})

@app.route("/", methods=["GET"])
def home():
    return "YouTube/Instagram/TikTok Downloader Backend is running!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
