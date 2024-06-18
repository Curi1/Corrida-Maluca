from resources.settings import TEXT_COLOR, BACKGROUND_COLOR


class Renderer:
    def __init__(self, screen, font):
        self.screen = screen
        self.font = font

    def draw_text(self, text, x, y):
        text_obj = self.font.render(text, 1, TEXT_COLOR)
        text_rect = text_obj.get_rect()
        text_rect.topleft = (x, y)
        self.screen.blit(text_obj, text_rect)

    def draw_background(self, road):
        self.screen.fill(BACKGROUND_COLOR)
        road.draw(self.screen)

    def draw_sprites(self, all_sprites):
        all_sprites.draw(self.screen)
