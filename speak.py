# speak.py
import edge_tts
import tempfile
import os

def say(text: str):
    try:
        print(f"🗣️ Speaking: {text}")
        communicate = edge_tts.Communicate(text, voice="en-US-AriaNeural")
        # Create a temporary MP3 file
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmpfile:
            tmp_path = tmpfile.name

        # Save the speech to file
        import asyncio
        asyncio.run(communicate.save(tmp_path))

        # Play the file with ffplay (non-blocking, no window)
        os.system(f"ffplay -nodisp -autoexit -loglevel quiet {tmp_path}")

        # Clean up
        os.remove(tmp_path)

    except Exception as e:
        print(f"❌ Text-to-speech failed: {e}")
