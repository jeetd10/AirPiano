<<<<<<< HEAD
# 🎹 AirPiano

> ✨ Play the piano with nothing but your fingers in the air — powered by computer vision and sound synthesis.

---

## 📸 Overview

**AirPiano** is a touchless piano experience that lets you use your **webcam and hand gestures** to play real piano chords. Built using **MediaPipe**, **OpenCV**, and **pygame**, this project brings together gesture recognition and sound playback for a magical musical experience.

No keyboard. No mouse. Just ✋🖐️ & 🎶.

---

## 🚀 Features

- ✅ Real-time hand detection using MediaPipe
- ✅ Finger tracking to map gestures to chords
- ✅ Sound playback using `.wav` samples for rich audio
- ✅ Smooth transitions and sustain between chords
- ✅ Support for both left and right hands

---

## 🧠 How it Works

- Detects your hand and finger positions using your webcam.
- Maps each finger to a predefined chord (e.g., thumb = D Major, index = E Minor).
- When you raise a finger, it plays the chord.
- When you lower it, the chord fades out naturally.


---

## 🛠️ Tech Stack

| Tool         | Purpose                              |
|--------------|---------------------------------------|
| Python       | Core programming language             |
| OpenCV       | Video frame capture and image processing |
| MediaPipe    | Real-time hand tracking               |
| pygame.mixer | Sound playback for `.wav` files       |

---

## 🧪 Setup Instructions

### ✅ 1. Clone the repository
```bash
git clone https://github.com/jeetd10/AirPiano.git
cd AirPiano
```

### ✅ 2. Create a virtual environment
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### ✅ 3. Install dependencies
```bash
pip install -r requirements.txt
```

### ✅ 4. Run the app
```bash
python main.py
```
--- 

🎵 Chord Mapping
Each hand maps fingers to specific chords:

Left Hand:                         Right Hand:
Thumb   → D Major                  Thumb   → D Major
Index   → E Minor                  Index   → E Minor
Middle  → F# Minor                 Middle  → F# Minor
Ring    → G Major                  Ring    → G Major
Pinky   → A Major                  Pinky   → A Major

---

📁 Folder Structure

AirPiano/
│
├── main.py              # App entry point
├── hand_tracker.py      # Hand detection module
├── chord_mapping.py     # Chord definitions
├── sound_player.py      # WAV file sound playback
├── sounds/              # Piano .wav sound samples
├── test_sound.py        # Sound testing utility
├── test_cam.py          # Camera testing utility
├── requirements.txt     # Python dependencies
└── README.md            # You’re reading it!

---

🙌 Credits
Created with ❤️ by Jeet Desai and Team

---




=======
# 🎹 AirPiano

> ✨ Play the piano with nothing but your fingers in the air — powered by computer vision and sound synthesis.

---

## 📸 Overview

**AirPiano** is a touchless piano experience that lets you use your **webcam and hand gestures** to play real piano chords. Built using **MediaPipe**, **OpenCV**, and **pygame**, this project brings together gesture recognition and sound playback for a magical musical experience.

No keyboard. No mouse. Just ✋🖐️ & 🎶.

---

## 🚀 Features

- ✅ Real-time hand detection using MediaPipe
- ✅ Finger tracking to map gestures to chords
- ✅ Sound playback using `.wav` samples for rich audio
- ✅ Smooth transitions and sustain between chords
- ✅ Support for both left and right hands

---

## 🧠 How it Works

- Detects your hand and finger positions using your webcam.
- Maps each finger to a predefined chord (e.g., thumb = D Major, index = E Minor).
- When you raise a finger, it plays the chord.
- When you lower it, the chord fades out naturally.


---

## 🛠️ Tech Stack

| Tool         | Purpose                              |
|--------------|---------------------------------------|
| Python       | Core programming language             |
| OpenCV       | Video frame capture and image processing |
| MediaPipe    | Real-time hand tracking               |
| pygame.mixer | Sound playback for `.wav` files       |

---

## 🧪 Setup Instructions

### ✅ 1. Clone the repository
```bash
git clone https://github.com/jeetd10/AirPiano.git
cd AirPiano
```

### ✅ 2. Create a virtual environment
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### ✅ 3. Install dependencies
```bash
pip install -r requirements.txt
```

### ✅ 4. Run the app
```bash
python main.py
```
--- 

🎵 Chord Mapping
Each hand maps fingers to specific chords:

Left Hand:                         Right Hand:
Thumb   → D Major                  Thumb   → D Major
Index   → E Minor                  Index   → E Minor
Middle  → F# Minor                 Middle  → F# Minor
Ring    → G Major                  Ring    → G Major
Pinky   → A Major                  Pinky   → A Major

---

📁 Folder Structure

AirPiano/
│
├── main.py              # App entry point
├── hand_tracker.py      # Hand detection module
├── chord_mapping.py     # Chord definitions
├── sound_player.py      # WAV file sound playback
├── sounds/              # Piano .wav sound samples
├── test_sound.py        # Sound testing utility
├── test_cam.py          # Camera testing utility
├── requirements.txt     # Python dependencies
└── README.md            # You’re reading it!

---

🙌 Credits
Created with ❤️ by Jeet Desai and Team

---






