import pygame
import time
import random

particles = 3
gravitationalPull = (500, 500)
particlePositions = []
width, height = 0, 0
screen = None


def initialize():
    global width, height, screen, particlePositions
    pygame.init()
    screen = pygame.display.set_mode((1000, 1000))
    pygame.display.set_caption("Gravitation")
    width, height = pygame.display.get_window_size()
    for i in range(particles):
        particlePositions.append((random.randint(0, width), random.randint(0, height)))
    for p in particlePositions:
        pygame.draw.rect(screen, (255, 255, 255), (p[0], p[1], 20, 20))
    pygame.display.flip()


initialize()
time.sleep(2)
