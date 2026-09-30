# egg.py
import pygame
import random
from settings import WIDTH, GRAVITY, EGG_RADIUS

class Egg:
    def __init__(self):
        self.radius = EGG_RADIUS
        self.x = random.randint(self.radius, WIDTH - self.radius)
        self.y = 0
        self.velocity = 0

    def update(self, dt):
        self.velocity += GRAVITY * dt
        self.y += self.velocity

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 200, 0), (int(self.x), int(self.y)), self.radius)
