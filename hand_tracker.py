# hand_tracker.py
import cv2
from cvzone.HandTrackingModule import HandDetector

class HandTracker:
    def __init__(self, detection_confidence=0.8):
        self.cap = cv2.VideoCapture(0)
        self.detector = HandDetector(detectionCon=detection_confidence)

    def read_frame(self):
        return self.cap.read()

    def detect_hands(self, img):
        return self.detector.findHands(img, draw=True)

    def fingers_up(self, hand):
        return self.detector.fingersUp(hand)

    def release(self):
        self.cap.release()
