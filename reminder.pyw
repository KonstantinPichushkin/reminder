import time
import pygame
from pathlib import Path


INTERVAL = 30 * 60  # seconds
VOLUME = 0.05
SCRIPT_DIR = Path(__file__).parent
AUDIO_FILE = SCRIPT_DIR / "goofy-ahh-ringtone.mp3"


pygame.mixer.init()
pygame.mixer.music.load(AUDIO_FILE)

while True:
    pygame.mixer.music.set_volume(VOLUME)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        time.sleep(0.1)

    time.sleep(INTERVAL)
