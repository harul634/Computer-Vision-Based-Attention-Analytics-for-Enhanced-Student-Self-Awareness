import cv2
import mediapipe as mp

class AttentionTracker:
    def __init__(self):
        self.face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)
        self.left_eye_indices = [33, 160, 158, 133, 153, 144]
        self.right_eye_indices = [362, 385, 387, 263, 373, 380]

    def get_eye_aspect_ratio(self, landmarks, indices, width, height):
        def to_point(index):
            return int(landmarks[index].x * width), int(landmarks[index].y * height)

        p = [to_point(i) for i in indices]
        # EAR formula
        ear = (cv2.norm((p[1][0] - p[5][0], p[1][1] - p[5][1])) +
               cv2.norm((p[2][0] - p[4][0], p[2][1] - p[4][1]))) / \
              (2.0 * cv2.norm((p[0][0] - p[3][0], p[0][1] - p[3][1])))
        return ear

    def analyze_frame(self, frame):
        height, width = frame.shape[:2]
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.face_mesh.process(rgb)

        if results.multi_face_landmarks:
            landmarks = results.multi_face_landmarks[0].landmark

            left_ear = self.get_eye_aspect_ratio(landmarks, self.left_eye_indices, width, height)
            right_ear = self.get_eye_aspect_ratio(landmarks, self.right_eye_indices, width, height)

            if left_ear > 0.2 and right_ear > 0.2:
                return "focused"

        return "distracted"
