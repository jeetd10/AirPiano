import pygame

pygame.mixer.init()
sound = pygame.mixer.Sound("sounds/d_major.wav")
print("🔊 Playing d_major.wav...")
sound.play()
pygame.time.wait(3000)
