# main.py

from hand_tracker import HandTracker
from sound_player import SoundPlayer
from chord_mapping import CHORDS
import cv2
import threading
import time

print("✅ Starting AirPiano")
print("🎥 Initializing webcam...")

# Sustain time in seconds
SUSTAIN_TIME = 2.0

# Initialize modules
tracker = HandTracker()
player = SoundPlayer()

# Test camera feed at startup
success, img = tracker.read_frame()
print(f"Webcam success: {success}")

# Track previous finger states to manage note on/off
prev_states = {hand: {finger: 0 for finger in CHORDS[hand]} for hand in CHORDS}

while True:
    success, img = tracker.read_frame()
    if not success:
        print("❌ Camera not capturing frames")
        continue

    hands, img = tracker.detect_hands(img)

    if hands:
        for hand in hands:
            hand_type = "left" if hand["type"] == "Left" else "right"
            fingers = tracker.fingers_up(hand)
            finger_names = list(CHORDS[hand_type].keys())

            for i, finger in enumerate(finger_names):
                chord = CHORDS[hand_type][finger]
                if fingers[i] == 1 and prev_states[hand_type][finger] == 0:
                    player.play_chord([chord.name])
                    print(f"🎶 Played {chord.name}")
                elif fingers[i] == 0 and prev_states[hand_type][finger] == 1:
                    threading.Thread(
                        target=player.stop_chord_after_delay,
                        args=([chord.name], SUSTAIN_TIME),
                        daemon=True
                    ).start()
                prev_states[hand_type][finger] = fingers[i]
    else:
        # If no hands detected, stop all chords
        for hand in CHORDS:
            for finger in CHORDS[hand]:
                chord = CHORDS[hand][finger]
                threading.Thread(
                    target=player.stop_chord_after_delay,
                    args=([chord.name], SUSTAIN_TIME),
                    daemon=True
                ).start()
        prev_states = {hand: {finger: 0 for finger in CHORDS[hand]} for hand in CHORDS}

    cv2.imshow("Air Piano", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Clean up
tracker.release()
cv2.destroyAllWindows()
player.quit()
