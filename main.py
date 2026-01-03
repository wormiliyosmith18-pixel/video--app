from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Video Generator API")

class VideoRequest(BaseModel):
    text: str

@app.get("/")
def home():
    return {"status": "FastAPI is running"}

@app.post("/generate-video")
def generate_video(data: VideoRequest):
    return {
        "message": "Video generation started",
        "your_text": data.text,
        "video_url": "https://example.com/fake-video.mp4"
    }
