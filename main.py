from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class VideoRequest(BaseModel):
    text: str

@app.get("/")
def home():
    return {"status": "API working"}

@app.post("/generate-video")
def generate_video(req: VideoRequest):

    script = f"""
Scene 1:
Voiceover: In the USA, one hospital visit can cost more than a new iPhone.
Visual: Man shocked seeing medical bill.
On-screen text: Medical bills are scary.

Scene 2:
Voiceover: Health insurance helps cover these huge costs.
Visual: Insurance shield protecting family.
On-screen text: Insurance saves money.

Scene 3:
Voiceover: Without insurance, savings disappear fast.
Visual: Empty wallet animation.
On-screen text: Be protected, stay insured.
"""

    return {
        "script":  video 
    }
