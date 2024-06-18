import pygame
from resources.settings import ROAD_WIDTH, SCREEN_HEIGHT, SCREEN_WIDTH, LEFT_SIDE_IMAGE_PATH, RIGHT_SIDE_IMAGE_PATH, \
    ASPHALT_IMAGE_PATH


class Road(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((ROAD_WIDTH, SCREEN_HEIGHT))
        self.asphalt = pygame.image.load(ASPHALT_IMAGE_PATH).convert()
        self.asphalt = pygame.transform.scale(self.asphalt, (ROAD_WIDTH, SCREEN_HEIGHT))
        self.left_side = pygame.image.load(LEFT_SIDE_IMAGE_PATH).convert()
        self.left_side = pygame.transform.scale(self.left_side, ((SCREEN_WIDTH - ROAD_WIDTH) // 2, SCREEN_HEIGHT))
        self.right_side = pygame.image.load(RIGHT_SIDE_IMAGE_PATH).convert()
        self.right_side = pygame.transform.scale(self.right_side, ((SCREEN_WIDTH - ROAD_WIDTH) // 2, SCREEN_HEIGHT))

        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

    def draw(self, screen):
        screen.blit(self.left_side, (0, 0))
        screen.blit(self.right_side, (SCREEN_WIDTH - (SCREEN_WIDTH - ROAD_WIDTH) // 2, 0))
        screen.blit(self.asphalt, ((SCREEN_WIDTH - ROAD_WIDTH) // 2, 0))
