# chord_mapping.py

from typing import Dict, List, Optional

# Define the type for a single chord (with optional name)
class Chord:
    def __init__(self, notes: List[int], name: str = ""):
        self.notes = notes
        self.name = name

    def __repr__(self):
        return f"{self.name or 'Chord'}: {self.notes}"


# Chord mappings for each hand and finger
CHORDS: Dict[str, Dict[str, Chord]] = {
    "left": {
        "thumb": Chord([62, 66, 69], "D Major"),
        "index": Chord([64, 67, 71], "E Minor"),
        "middle": Chord([66, 69, 73], "F# Minor"),
        "ring": Chord([67, 71, 74], "G Major"),
        "pinky": Chord([69, 73, 76], "A Major")
    },
    "right": {
        "thumb": Chord([62, 66, 69], "D Major"),
        "index": Chord([64, 67, 71], "E Minor"),
        "middle": Chord([66, 69, 73], "F# Minor"),
        "ring": Chord([67, 71, 74], "G Major"),
        "pinky": Chord([69, 73, 76], "A Major")
    }
}


def get_chord(hand: str, finger: str) -> Optional[Chord]:
    """
    Safely retrieve a chord based on hand and finger.
    Returns None if invalid input is provided.
    """
    hand = hand.lower()
    finger = finger.lower()
    return CHORDS.get(hand, {}).get(finger)


# Example usage (for debugging or testing)
if __name__ == "__main__":
    chord = get_chord("left", "index")
    if chord:
        print(f"Playing {chord.name}: {chord.notes}")
    else:
        print("Invalid hand or finger input.")
# chord_mapping.py

from typing import Dict, List, Optional

class Chord:
    def __init__(self, notes: List[int], name: str = ""):
        self.notes = notes
        self.name = name

    def __repr__(self):
        return f"{self.name or 'Chord'}: {self.notes}"


CHORDS: Dict[str, Dict[str, Chord]] = {
    "left": {
        "thumb": Chord([62, 66, 69], "D Major"),
        "index": Chord([64, 67, 71], "E Minor"),
        "middle": Chord([66, 69, 73], "F# Minor"),
        "ring": Chord([67, 71, 74], "G Major"),
        "pinky": Chord([69, 73, 76], "A Major")
    },
    "right": {
        "thumb": Chord([62, 66, 69], "D Major"),
        "index": Chord([64, 67, 71], "E Minor"),
        "middle": Chord([66, 69, 73], "F# Minor"),
        "ring": Chord([67, 71, 74], "G Major"),
        "pinky": Chord([69, 73, 76], "A Major")
    }
}


def get_chord(hand: str, finger: str) -> Optional[Chord]:
    hand = hand.lower()
    finger = finger.lower()
    return CHORDS.get(hand, {}).get(finger)
