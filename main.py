
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import cv2
import time
import json
from datetime import datetime, timedelta
from src.detection.attention_tracker import AttentionTracker
from src.detection.phone_detector import PhoneDetector

def calibration_screen():
    cap = cv2.VideoCapture(0)
    print("Calibration: Adjust your lighting and face position. Press 'c' to continue.")
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        cv2.putText(frame, "Calibration Mode - Press 'c' when ready", (30, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)
        cv2.imshow("Calibration", frame)
        if cv2.waitKey(1) & 0xFF == ord('c'):
            break
    cap.release()
    cv2.destroyAllWindows()

attention_tracker = AttentionTracker()
phone_detector = PhoneDetector('models/yolov5n.pt')

calibration_screen()  # Run calibration

cap = cv2.VideoCapture(0)
session_log = {}

print("Session started. Press 'q' to stop.")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    attention_status = attention_tracker.analyze_frame(frame)
    phone_status = phone_detector.detect_phone(frame)

    timestamp = time.strftime("%Y-%m-%dT%H:%M:%S")
    if phone_status == "phone_detected":
        session_log[timestamp] = "distracted"
    else:
        session_log[timestamp] = attention_status

    cv2.putText(frame, f"Attention: {session_log[timestamp]}", (30, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.imshow("FocusFlow - Live Monitor", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

# Save log
os.makedirs("data/logs", exist_ok=True)
log_path = "data/logs/session_log.json"
with open(log_path, "w") as f:
    json.dump(session_log, f, indent=4)

# Generate feedback summary
focus_duration = timedelta(0)
distract_duration = timedelta(0)
timestamps = sorted(session_log.keys())
for i in range(1, len(timestamps)):
    current_time = datetime.fromisoformat(timestamps[i])
    prev_time = datetime.fromisoformat(timestamps[i - 1])
    time_diff = current_time - prev_time

    if session_log[timestamps[i - 1]] == 'focused':
        focus_duration += time_diff
    else:
        distract_duration += time_diff

summary = {
    "Total Focus Time (minutes)": round(focus_duration.total_seconds() / 60, 2),
    "Total Distracted Time (minutes)": round(distract_duration.total_seconds() / 60, 2),
    "Session Duration (minutes)": round((focus_duration + distract_duration).total_seconds() / 60, 2),
    "Focus Percentage": round((focus_duration.total_seconds() / (focus_duration + distract_duration).total_seconds()) * 100, 2)
}

summary_path = "data/logs/focus_summary.json"
with open(summary_path, "w") as f:
    json.dump(summary, f, indent=4)

# Update streak file
streak_path = "data/logs/streak.json"
streak = {"current_streak": 0}

if os.path.exists(streak_path):
    with open(streak_path, "r") as f:
        streak = json.load(f)

if summary["Focus Percentage"] >= 90:
    streak["current_streak"] += 1
else:
    streak["current_streak"] = 0

with open(streak_path, "w") as f:
    json.dump(streak, f, indent=4)
