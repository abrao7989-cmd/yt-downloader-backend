# YouTube Downloader Backend

Flask backend for YouTube/Social Downloader API using RapidAPI.

## Endpoints
- `/` → Health check
- `/download?url=<video_url>&format=mp4` → Get video info

## Deploy on Render
1. Fork or upload this repo to GitHub.
2. Go to [Render](https://render.com).
3. Create new **Web Service** → Connect GitHub → Select this repo.
4. Build Command:  
   ```
   pip install -r requirements.txt
   ```
5. Start Command:  
   ```
   gunicorn app:app
   ```
6. Add environment variable:  
   ```
   RAPIDAPI_KEY = your_api_key_here
   ```
7. Deploy 🚀
