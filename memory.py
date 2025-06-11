# memory.py
import json
from datetime import datetime
from pathlib import Path

LOG_FILE = Path("chat_log.json")

def log_message(role, message):
    entry = {
        "timestamp": datetime.now().isoformat(timespec="seconds"),
        "role": role,
        "message": message
    }

    # Load old entries
    if LOG_FILE.exists():
        with open(LOG_FILE, "r", encoding="utf-8") as f:
            history = json.load(f)
    else:
        history = []

    # Append and save
    history.append(entry)
    with open(LOG_FILE, "w", encoding="utf-8") as f:
        json.dump(history, f, indent=2)

def load_memory():
    if LOG_FILE.exists():
        with open(LOG_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []
