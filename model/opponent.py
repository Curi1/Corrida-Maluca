import pygame
import random
from settings import OPPONENT_WIDTH, OPPONENT_HEIGHT, OPPONENT_SPEED_MIN, OPPONENT_SPEED_MAX, SCREEN_WIDTH, ROAD_WIDTH, \
    SCREEN_HEIGHT


class Opponent(pygame.sprite.Sprite):
    def __init__(self, image_path):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(image_path), (OPPONENT_WIDTH, OPPONENT_HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint((SCREEN_WIDTH - ROAD_WIDTH) // 2,
                                     (SCREEN_WIDTH + ROAD_WIDTH) // 2 - OPPONENT_WIDTH)
        self.rect.y = -OPPONENT_HEIGHT
        self.y_speed = random.randint(OPPONENT_SPEED_MIN, OPPONENT_SPEED_MAX)

    def update(self):
        self.rect.y += self.y_speed
        if self.rect.top > SCREEN_HEIGHT:
            self.kill()
