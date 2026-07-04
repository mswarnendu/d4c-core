from pathlib import Path

import sounddevice as sd
from scipy.io.wavfile import write
from voice.speak import speak
import wave
import os
import os
import sys
from datetime import datetime
import subprocess
import os
import platform
from playsound import playsound
from pathlib import Path
import sys


def build_filename(save_path):
    if not save_path or save_path.strip() == "":
        save_path = "recording"

    save_path = save_path.replace(" ", "_").replace("/", "_")

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    return f"{save_path}_{timestamp}"


def convert_time(value, unit):
    unit = unit.lower().strip()

    minutes_units = {"min", "mins", "minute", "minutes"}
    seconds_units = {"sec", "secs", "second", "seconds"}

    if unit in minutes_units:
        return value * 60
    if unit in seconds_units:
        return value

    raise ValueError(f"Unsupported time unit: {unit}")


def record(s_file_name=f"unnamed_recording_{datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}", duration_value=1, duration_unit="seconds"):
    speak("Starting recording.")

    sample_rate = 44100
    duration_seconds = convert_time(duration_value, duration_unit)

    os.makedirs("recordings", exist_ok=True)

    file_path = f"recordings/{s_file_name}.wav"

    audio_data = sd.rec(
        int(duration_seconds * sample_rate),
        samplerate=sample_rate,
        channels=1,
        dtype='int16'
    )

    sd.wait()
    speak("Recording finished.")

    write(file_path, sample_rate, audio_data)

    speak(f"Saved as {s_file_name}.wav")


def open_recordings_folder(relative_path: str = "recordings"):

    base_dir = Path(__file__).resolve().parents[1]
    target_dir = (base_dir / relative_path).resolve()

    if not target_dir.exists():
        print(f"Error: The path '{target_dir}' does not exist.")
        target_dir.mkdir(parents=True, exist_ok=True)
        return

    system = platform.system()

    try:
        if system == "Windows":
            subprocess.run(["explorer", str(target_dir)])

        elif system == "Darwin":
            subprocess.run(["open", str(target_dir)])

        elif system == "Linux":
            subprocess.run(["xdg-open", str(target_dir)])

        else:
            print(f"Unsupported OS: {system}")

    except Exception as e:
        print(f"Failed to open folder: {e}")

    return "Opened recordings folder."
