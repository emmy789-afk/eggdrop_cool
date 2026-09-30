import pygame
import sys
import random

from settings import WIDTH, HEIGHT, FPS
from egg import Egg
from player import Player

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Egg Drop - Emmanuel Edition")
clock = pygame.time.Clock()

player = Player()
eggs = []
spawn_timer = 0
spawn_interval = 1.0
score = 0

def check_collisions():
    global score
    for egg in eggs[:]:
        if (player.y <= egg.y <= player.y + player.height and
            player.x <= egg.x <= player.x + player.width):
            score += 1
            eggs.remove(egg)
        elif egg.y > HEIGHT:
            eggs.remove(egg)
            print("Egg broke!")

running = True
while running:
    dt = clock.tick(FPS) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player.move()

    spawn_timer += dt
    if spawn_timer >= spawn_interval:
        eggs.append(Egg())
        spawn_timer = 0

    for egg in eggs:
        egg.update(dt)

    check_collisions()

    screen.fill((255, 255, 255))
    player.draw(screen)

    for egg in eggs:
        egg.draw(screen)

    pygame.display.flip()

pygame.quit()
sys.exit()

