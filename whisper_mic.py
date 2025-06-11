import sounddevice as sd
import scipy.io.wavfile as wav
import tempfile
import subprocess

def transcribe_from_mic(duration=5, sample_rate=16000):
    print("🎤 Recording for 5 seconds. Please speak now...")

    try:
        recording = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype='int16')
        sd.wait()
    except Exception as e:
        print(f"❌ Microphone recording failed: {e}")
        return ""

    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as f:
        wav.write(f.name, sample_rate, recording)
        tmp_path = f.name

    print(f"🔊 Audio saved to: {tmp_path}")
    print("🧠 Transcribing with whisper.cpp...")

    result = subprocess.run([
        "./whisper.cpp/build/bin/whisper-cli",
        "-m", "./whisper.cpp/models/ggml-base.en.bin",
        "-f", tmp_path,
        "-nt",  # no timestamps
        "-l", "en"
    ], capture_output=True, text=True)

    if result.returncode == 0:
        return result.stdout.strip()
    else:
        print("❌ Transcription failed:", result.stderr)
        return ""
