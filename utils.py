import json
from datetime import datetime

def load_events(filepath):
    try:
        with open(filepath, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_events(filepath, events):
    with open(filepath, 'w') as f:
        json.dump(events, f, indent=4)

def sort_events(events):
    return sorted(events, key=lambda x: x['start_time'])

def is_due_within_one_hour(event):
    now = datetime.now()
    start = datetime.fromisoformat(event['start_time'])
    return 0 <= (start - now).total_seconds() <= 3600

def load_events(filepath):
    try:
        with open(filepath, 'r') as f:
            content = f.read().strip()
            return json.loads(content) if content else []
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []
