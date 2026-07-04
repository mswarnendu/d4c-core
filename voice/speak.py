import os
import asyncio
import edge_tts
from playsound import playsound


async def generate_speech(TEXT, VOICE="en-GB-RyanNeural", OUTPUT_FILE="spoken_text.mp3"):
    communicate = edge_tts.Communicate(
        TEXT, VOICE, rate="-10%", pitch="-5Hz")
    await communicate.save(OUTPUT_FILE)


def speak(TEXT):
    asyncio.run(generate_speech(TEXT))
    playsound("spoken_text.mp3")
    os.remove("spoken_text.mp3")