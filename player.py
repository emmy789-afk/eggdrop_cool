import pygame
from settings import WIDTH, BASKET_WIDTH, BASKET_HEIGHT, BASKET_SPEED

class Player:
    def __init__(self):
        self.width = BASKET_WIDTH
        self.height = BASKET_HEIGHT
        self.x = WIDTH // 2 - self.width // 2
        self.y = 550

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.x -= BASKET_SPEED
        if keys[pygame.K_RIGHT]:
            self.x += BASKET_SPEED

        self.x = max(0, min(self.x, WIDTH - self.width))

    def draw(self, screen):
        pygame.draw.rect(screen, (0, 0, 0), (self.x, self.y, self.width, self.height))
