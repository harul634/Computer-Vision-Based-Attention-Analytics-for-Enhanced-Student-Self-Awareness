FocusFlow
From Distraction to Discipline
📋 Table of Contents

Overview
Problem Statement
Solution Architecture
Features
Technology Stack
Installation
Usage
Demo
Performance Metrics
Limitations
Future Work
Team
License

🎯 Overview
FocusFlow is a privacy-first, real-time attention tracking system designed to help students improve their academic discipline during online learning. Acting as a "fitness tracker" for attention, FocusFlow uses lightweight computer vision models to monitor focus and provide actionable insights through an intuitive dashboard.
Why FocusFlow?
Academic success heavily relies on consistent focus and self-awareness. Without knowing when or how they lose focus, students can't build better habits. FocusFlow addresses this gap by:

Providing real-time attention feedback
Tracking focus patterns over time
Identifying distraction triggers
Gamifying learning with achievement badges

🔍 Problem Statement
"Online classes lack real-time tools to monitor student engagement"
Key Challenges:

Many ASU students study online but struggle to maintain focus
Distractions like phone use, web browsing, or zoning out are invisible to instructors and students themselves
No existing tools offer real-time feedback based on actual visual attention
Traditional methods (timers, click-tracking) cannot measure real-time visual focus

🏗️ Solution Architecture
┌─────────────┐
│   Webcam    │
│    Input    │
└──────┬──────┘
       │
       ├──────────────────┬─────────────────┐
       │                  │                 │
┌──────▼──────┐   ┌──────▼──────┐   ┌─────▼─────┐
│  Attention  │   │   Focused   │   │ FocusFlow │
│  Tracking   │   │     or      │   │ Dashboard │
│             │   │ Distracted? │   │           │
└─────────────┘   └─────────────┘   └─────┬─────┘
                                          │
                                    ┌─────▼─────┐
                                    │  Session  │
                                    │  Summary  │
                                    │  Screen   │
                                    └───────────┘
Processing Pipeline:

Webcam Capture: Real-time video stream processing
Attention Tracking: Facial and eye feature detection using MediaPipe Face Mesh
Distraction Detection: Mobile phone detection using YOLOv5-lite
Data Logging: Local storage of focus and distraction events
Visualization: Dashboard with real-time analytics and gamification

✨ Features
Core Functionality

✅ Real-time Attention Monitoring: Track head position and gaze orientation
✅ Distraction Detection: Identify external distractions (e.g., mobile phone usage)
✅ Focus Analytics: Detailed session summaries and trend analysis
✅ Privacy-First Design: 100% local processing, no video storage
✅ Gamification: Achievement badges and streak tracking

Dashboard Insights

Focus trend over time (line chart)
Focus vs. Distraction ratio (pie chart)
Session summary metrics:

Total focus time
Total distracted time
Session duration
Focus percentage


Badge achievement system

🛠️ Technology Stack
Computer Vision Models

MediaPipe Face Mesh: Facial landmark detection and gaze tracking
YOLOv5-lite: Lightweight object detection for distraction identification

Libraries & Frameworks
opencv-python
mediapipe
torch
ultralytics
numpy
pandas
matplotlib
Platform

Processing: Local device only (no cloud/server required)
Hardware: Standard laptop webcam
OS Support: Cross-platform (Windows, macOS, Linux)

📦 Installation
Prerequisites

Python 3.8 or higher
Webcam-enabled device
4GB+ RAM recommended

Setup Instructions

Clone the repository

bashgit clone https://github.com/yourusername/focusflow.git
cd focusflow

Create virtual environment

bashpython -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

Install dependencies

bashpip install -r requirements.txt

Download model weights (if not included)

bash# YOLOv5-lite weights will be downloaded automatically on first run
🚀 Usage
Basic Usage

Start FocusFlow

bashpython focusflow.py

Calibration Mode (optional)
Press 'C' when ready to begin calibration. Look directly at the screen for 5 seconds.
Start Session
Press 'S' to start tracking your focus session.
End Session
Press 'Q' to quit and view your session summary.

Configuration
Edit config.yaml to customize:
yaml# Attention thresholds
gaze_threshold: 15  # degrees
blink_threshold: 0.2

# Distraction detection
phone_confidence: 0.5
detection_fps: 15

# Privacy settings
save_logs: true
save_video: false  # Always false for privacy
🎬 Demo
FocusFlow monitors attention in real-time, detecting three primary states:

Focused: User is looking at the screen with proper head position
Distracted (Looking Away): User's gaze is oriented away from the screen
Distracted (Phone): Mobile phone detected in the camera frame

Dashboard Features
The dashboard provides comprehensive session analytics including:

Focus trend visualization over time
Focus vs. Distraction ratio analysis
Detailed session metrics (focus time, distraction time, duration, percentage)
Achievement badges and streak tracking

Sample session data: 62.9% focus rate over a 33-minute study session
📊 Performance Metrics
Success Metrics

✅ Consistent real-time focus and distraction detection
✅ <1 second system response time for live feedback
✅ Validated across different lighting conditions
✅ Tested with various face orientations

Resource Requirements

CPU Usage: ~15-25% (single core)
RAM: ~500MB
Disk Space: Minimal (~50MB for logs)
Network: None required

Accuracy (Internal Testing)

Face detection: ~95% under normal lighting
Gaze estimation: ~85% accuracy ±10°
Phone detection: ~90% precision

⚠️ Limitations
Current Constraints

Environmental Sensitivity

Performance depends on lighting conditions
Requires adequate webcam quality
Best results in well-lit environments


Privacy Considerations

Even with local-only processing, webcam monitoring may raise concerns
Requires explicit user consent


Validation Scope

Testing based on manual internal validation
Not validated on large-scale datasets
Limited diversity in testing scenarios



🔮 Future Work
Planned Enhancements

Expanded Application Domains

Corporate training programs
Professional certification platforms
Remote proctoring solutions


Advanced Features

Emotion detection (boredom, confusion, engagement)
Multi-user classroom monitoring
Automated attendance through facial recognition
Integration with learning management systems (Canvas, Blackboard)


Technical Improvements

Enhanced low-light performance
Mobile application support
Cloud-based analytics (with user consent)
API for third-party integrations


Research Directions

Correlation studies between attention patterns and academic performance
A/B testing for different feedback mechanisms
Cross-cultural validation studies



👥 Team
Team 104 - CIS 515
This project was developed as part of the Computer Vision course at Arizona State University's W.P. Carey School of Business.
Team Contributions:

CV Model Implementation & Demo
Solution Architecture & Validation
Problem Definition & Research
Limitations Analysis & Future Work

📄 License
This project is licensed under the MIT License - see the LICENSE file for details.

🙏 Acknowledgments

Arizona State University - CIS 515 Course
MediaPipe team for facial landmark detection
Ultralytics for YOLOv5
Open-source community for various tools and libraries

🌟 Star History
If you find FocusFlow helpful, please consider giving it a star ⭐

Disclaimer: FocusFlow is designed as an educational tool to help students improve focus. It should be used with informed consent and in compliance with applicable privacy regulations. This tool is not intended to replace professional educational or psychological support.
Privacy Notice: All processing occurs locally on your device. No video data is transmitted or stored externally. Session logs are stored locally and can be deleted at any time.

Built with ❤️ by Team 104 at Arizona State University
