from ultralytics import YOLO

class PhoneDetector:
    def __init__(self, model_path):
        self.model = YOLO(model_path)

    def detect_phone(self, frame):
        results = self.model(frame)
        for result in results:
            if any(label == 67 for label in result.boxes.cls.cpu().numpy()):  # 67 = COCO class for "cell phone"
                return "phone_detected"
        return "no_phone"
