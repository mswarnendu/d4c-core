import pygame
import math
import threading
from utils.utils import wait_for_wake, ask_user
from voice.speak import speak
from datetime import datetime

pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("D4C")
clock = pygame.time.Clock()

min_radius = 40
max_radius = 50
pulse_speed = 0.05

pygame.draw.circle(screen, (0, 0, 255), (300, 300), min_radius)

running = True
t = 0


def d4c_loop():
    global running

    while running:
        wait_for_wake()

        if not running:
            break

        speak("All systems are operational. How may I help you?")

        while running:
            prompt = ask_user()

            if not prompt:
                continue

            prompt = prompt.lower()

            if "terminate" in prompt or "go to sleep" in prompt:
                speak("Going back to standby.")
                running = False
                break


threading.Thread(target=d4c_loop, daemon=True).start()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    sine_wave = (math.sin(t) + 1) / 2
    current_radius = int(
        min_radius + sine_wave * (max_radius - min_radius)
    )

    screen.fill((30, 30, 30))
    pygame.draw.circle(screen, (255, 165, 0), (300, 300), current_radius)

    pygame.display.flip()
    clock.tick(60)
    t += pulse_speed

pygame.quit()
