
# FocusFlow – From Distraction to Discipline

## Modules

- **Attention Tracking** – Uses MediaPipe to detect if user is looking at the screen.
- **Phone Detection** – Uses YOLOv5-lite to check if phone is in frame.
- **Session Logger** – Records timestamps with focus/distracted labels.
- **Dashboard** – Streamlit app visualizes focus logs.

## Usage

1. Run `src/main.py` to start a session.
2. Press 'q' to end and save log.
3. Run `streamlit run dashboard/streamlit_app.py` to visualize.

## Requirements

```bash
pip install streamlit mediapipe opencv-python ultralytics matplotlib
```
