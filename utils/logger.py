import datetime
import os

LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

def log_event(message):
    timestamp = datetime.datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
    log_message = f"{timestamp} {message}\n"
    print(log_message.strip())
    with open(os.path.join(LOG_DIR, "events.log"), "a", encoding='utf-8') as f:
        f.write(log_message)
