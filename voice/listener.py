import time
import numpy as np
import sounddevice as sd
import webrtcvad
from faster_whisper import WhisperModel

SAMPLE_RATE = 16000
FRAME_MS = 30
FRAME_SIZE = int(SAMPLE_RATE * FRAME_MS / 1000)

START_FRAMES = 2
SILENCE_FRAMES = 10
MIN_SPEECH_FRAMES = 6
MAX_SECONDS = 10

vad = webrtcvad.Vad(1)

model = WhisperModel(
    "base.en",
    device="cpu",
    compute_type="int8"
)


def listen_once():
    speech_frames = []
    speaking = False
    speech_count = 0
    silence_count = 0

    start_time = time.time()

    print("Waiting for speech...")

    with sd.InputStream(
        samplerate=SAMPLE_RATE,
        blocksize=FRAME_SIZE,
        dtype="int16",
        channels=1,
    ) as stream:

        while True:
            if time.time() - start_time > MAX_SECONDS:
                break

            frame, _ = stream.read(FRAME_SIZE)

            frame = np.asarray(frame, dtype=np.int16)
            frame_bytes = frame.tobytes()

            if len(frame_bytes) != FRAME_SIZE * 2:
                continue

            try:
                is_speech = vad.is_speech(frame_bytes, SAMPLE_RATE)
            except Exception:
                continue

            if not speaking:
                if is_speech:
                    speech_count += 1
                    if speech_count >= START_FRAMES:
                        speaking = True
                        print("Listening...")
                        speech_frames.append(frame_bytes)
                else:
                    speech_count = 0
                continue

            speech_frames.append(frame_bytes)

            if is_speech:
                silence_count = 0
            else:
                silence_count += 1
                if silence_count >= SILENCE_FRAMES:
                    break

    if len(speech_frames) < MIN_SPEECH_FRAMES:
        return ""
    audio = np.frombuffer(b"".join(speech_frames),
                          dtype=np.int16).astype(np.float32)
    audio /= 32768.0

    peak = np.max(np.abs(audio))
    if peak > 0:
        audio /= peak

    print("Transcribing...")

    segments, _ = model.transcribe(
        audio,
        language="en",
        beam_size=1,
        vad_filter=True
    )

    text = "".join(s.text for s in segments).strip()

    print(f"Heard: {text}")
    return text
