# YouTube/Instagram/TikTok Downloader Backend

This is a Flask backend to connect with the RapidAPI Auto Download All In One API.

## Endpoints

- `/` → Health check
- `/download?url=<video_url>&format=mp4` → Download video/audio info

## Deployment

1. Push code to GitHub.
2. Connect repo to Render.com.
3. Add environment variable in Render:
   - `RAPIDAPI_KEY` = your RapidAPI key
4. Deploy!
