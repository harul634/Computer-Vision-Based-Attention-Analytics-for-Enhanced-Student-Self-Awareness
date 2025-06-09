
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import json
import os
from datetime import datetime

st.title("📊 FocusFlow Dashboard")
st.markdown("Visualize your focus session results and summary insights.")

# Load session log
log_file = "data/logs/session_log.json"
summary_file = "data/logs/focus_summary.json"
streak_file = "data/logs/streak.json"

if os.path.exists(log_file):
    with open(log_file, "r") as f:
        log = json.load(f)

    df = pd.DataFrame([
        {"timestamp": datetime.fromisoformat(ts), "status": status}
        for ts, status in log.items()
    ])
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df.set_index('timestamp', inplace=True)
    df['focused'] = df['status'].apply(lambda x: 1 if x == 'focused' else 0)

    st.subheader("📈 Focus Trend Over Time")
    st.line_chart(df['focused'])

    focused = df['focused'].sum()
    distracted = len(df) - focused

    st.subheader("📊 Focus vs Distraction")
    fig, ax = plt.subplots()
    ax.pie([focused, distracted], labels=["Focused", "Distracted"], autopct='%1.1f%%', startangle=90)
    ax.axis("equal")
    st.pyplot(fig)

    if os.path.exists(summary_file):
        with open(summary_file, "r") as f:
            summary = json.load(f)

        st.subheader("📝 Session Summary")
        for key, value in summary.items():
            st.write(f"**{key}**: {value}")

    if os.path.exists(streak_file):
        with open(streak_file, "r") as f:
            streak = json.load(f)

        st.subheader("🔥 Focus Streak")
        st.write(f"**Current Focus Streak**: {streak['current_streak']} sessions with >90% focus")

        st.subheader("🏅 Badges Earned")
        total_focus_minutes = summary.get("Total Focus Time (minutes)", 0)
        if total_focus_minutes >= 300:
            st.success("🥇 Focus Master: 5+ hours of focused time!")
        elif total_focus_minutes >= 180:
            st.success("🏅 Focus Pro: 3+ hours of focused time!")
        elif total_focus_minutes >= 60:
            st.success("🎖️ Focus Beginner: 1+ hour of focused time!")
        else:
            st.info("🔰 Keep going to earn badges!")

else:
    st.warning("No session log found. Please run a session first.")
