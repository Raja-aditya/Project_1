import threading
import time
from utils import load_events, is_due_within_one_hour

def check_reminders(filepath):
    while True:
        events = load_events(filepath)
        for event in events:
            if is_due_within_one_hour(event):
                print(f"🔔 Reminder: {event['title']} is due at {event['start_time']}")
        time.sleep(60)

def start_reminder_thread(filepath):
    thread = threading.Thread(target=check_reminders, args=(filepath,), daemon=True)
    thread.start()
