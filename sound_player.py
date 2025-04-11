import pygame
import os

class SoundPlayer:
    def __init__(self):
        pygame.mixer.init()
        pygame.mixer.set_num_channels(16)  # Allow multiple simultaneous sounds

        sound_folder = os.path.join(os.getcwd(), "sounds")
        print(f"🔍 Looking for sounds in: {sound_folder}")

        self.sounds = {
            "D Major": self.load_sound("d_major.wav", sound_folder),
            "E Minor": self.load_sound("e_minor.wav", sound_folder),
            "F# Minor": self.load_sound("f_sharp_minor.wav", sound_folder),
            "G Major": self.load_sound("g_major.wav", sound_folder),
            "A Major": self.load_sound("a_major.wav", sound_folder),
        }

    def load_sound(self, filename, folder):
        path = os.path.join(folder, filename)
        if os.path.exists(path):
            print(f"✅ Loaded: {filename}")
            return pygame.mixer.Sound(path)
        else:
            print(f"❌ Missing: {filename}")
            return None

    def play_chord(self, chord_names):
        for name in chord_names:
            sound = self.sounds.get(name)
            if sound:
                sound.set_volume(1.0)
                sound.play()
            else:
                print(f"⚠️ Chord '{name}' not loaded")

    def stop_chord_after_delay(self, chord_names, delay):
        pygame.time.wait(int(delay * 1000))
        # Stop all sounds — pygame.mixer doesn't allow stopping a specific one easily
        pygame.mixer.stop()

    def quit(self):
        pygame.mixer.quit()
