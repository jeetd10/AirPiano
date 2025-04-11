# sound_player.py

import pygame # type: ignore
import time
import os

class SoundPlayer:
    def __init__(self, sound_folder="sounds"):
        pygame.mixer.init()
        self.sounds = {
            "D Major": pygame.mixer.Sound(os.path.join(sound_folder, "d_major.wav")),
            "E Minor": pygame.mixer.Sound(os.path.join(sound_folder, "e_minor.wav")),
            "F# Minor": pygame.mixer.Sound(os.path.join(sound_folder, "f_sharp_minor.wav")),
            "G Major": pygame.mixer.Sound(os.path.join(sound_folder, "g_major.wav")),
            "A Major": pygame.mixer.Sound(os.path.join(sound_folder, "a_major.wav")),
        }

    def play_chord(self, name):
        if name in self.sounds:
            self.sounds[name].play()
    
    def stop_chord_after_delay(self, name, delay):
        time.sleep(delay)
        if name in self.sounds:
            self.sounds[name].stop()

    def quit(self):
        pygame.mixer.quit()
