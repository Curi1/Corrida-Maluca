import pygame
from resources.settings import PLAYER_WIDTH, PLAYER_HEIGHT, PLAYER_SPEED, SCREEN_WIDTH, SCREEN_HEIGHT, ROAD_WIDTH


class Player(pygame.sprite.Sprite):
    def __init__(self, image_path):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(image_path), (PLAYER_WIDTH, PLAYER_HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT - PLAYER_HEIGHT)

    def update(self, keys):
        if keys[pygame.K_LEFT] and self.rect.left > (SCREEN_WIDTH - ROAD_WIDTH) // 2:
            self.rect.x -= PLAYER_SPEED
        if keys[pygame.K_RIGHT] and self.rect.right < (SCREEN_WIDTH + ROAD_WIDTH) // 2:
            self.rect.x += PLAYER_SPEED
        if keys[pygame.K_UP] and self.rect.top > 0:
            self.rect.y -= PLAYER_SPEED
        if keys[pygame.K_DOWN] and self.rect.bottom < SCREEN_HEIGHT:
            self.rect.y += PLAYER_SPEED
