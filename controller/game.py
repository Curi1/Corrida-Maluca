import pygame
import random
import os
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, FPS, FONT_NAME, FONT_SIZE, MUSIC_PATH, CRASH_SOUND_PATH, \
    CHUCKLE_SOUND_PATH, HIGH_SCORE_FILE, INITIAL_LIVES, PLAYER_HEIGHT
from model.player import Player
from model.opponent import Opponent
from view.road import Road
from view.renderer import Renderer

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Road Fighter")
        self.clock = pygame.time.Clock()
        self.running = True
        self.font = pygame.font.SysFont(FONT_NAME, FONT_SIZE)
        self.renderer = Renderer(self.screen, self.font)

        self.player = Player("assets/player_car.png")
        self.road = Road()

        self.all_sprites = pygame.sprite.Group()
        self.opponents = pygame.sprite.Group()
        self.all_sprites.add(self.player)

        # Sons
        self.crash_sound = pygame.mixer.Sound(CRASH_SOUND_PATH)
        self.chuckle_sound = pygame.mixer.Sound(CHUCKLE_SOUND_PATH)
        pygame.mixer.music.load(MUSIC_PATH)

        # Pontuação e vidas
        self.score = 0
        self.high_score = self.load_high_score()
        self.lives = INITIAL_LIVES

    def load_high_score(self):
        if os.path.exists(HIGH_SCORE_FILE):
            try:
                with open(HIGH_SCORE_FILE, 'r') as file:
                    return int(file.readline().strip())
            except ValueError:
                return 0
        return 0

    def save_high_score(self):
        with open(HIGH_SCORE_FILE, 'w') as file:
            file.write(str(self.high_score))

    def run(self):
        self.show_start_screen()
        pygame.mixer.music.play(-1, 0.0)
        while self.running:
            self.reset_game()
            self.play_game()
            if self.lives <= 0:
                self.show_game_over_screen()
        pygame.quit()

    def show_start_screen(self):
        self.renderer.draw_background(self.road)
        self.renderer.draw_text("RALLY RACE", SCREEN_WIDTH / 3 - 30, SCREEN_HEIGHT / 3)
        self.renderer.draw_text("Press any key to begin", SCREEN_WIDTH / 3, SCREEN_HEIGHT / 3 + 30)
        self.renderer.draw_text(f"Score to beat: {self.high_score}", SCREEN_WIDTH / 3, SCREEN_HEIGHT / 3 + 60)
        pygame.display.flip()
        self.wait_for_key()

    def show_game_over_screen(self):
        self.renderer.draw_background(self.road)
        self.renderer.draw_text("GAME OVER", SCREEN_WIDTH / 3, SCREEN_HEIGHT / 3)
        self.renderer.draw_text("Press any key to try again.", SCREEN_WIDTH / 3 - 80, SCREEN_HEIGHT / 3 + 30)
        pygame.display.flip()
        self.wait_for_key()
        self.lives = INITIAL_LIVES
        self.score = 0

    def wait_for_key(self):
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    waiting = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False
                        waiting = False
                    waiting = False

    def reset_game(self):
        self.all_sprites.empty()
        self.opponents.empty()
        self.all_sprites.add(self.player)
        self.player.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT - PLAYER_HEIGHT)

    def play_game(self):
        while self.lives > 0 and self.running:
            self.events()
            self.update()
            self.draw()
            self.clock.tick(FPS)

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        keys = pygame.key.get_pressed()
        for sprite in self.all_sprites:
            if isinstance(sprite, Player):
                sprite.update(keys)
            else:
                sprite.update()

        if random.randint(1, 50) == 1:
            self.add_opponent()

        if pygame.sprite.spritecollideany(self.player, self.opponents):
            self.crash_sound.play()
            self.lives -= 1
            if self.lives > 0:
                self.reset_game()
            else:
                if self.score > self.high_score:
                    self.high_score = self.score
                    self.save_high_score()
                self.running = False

        self.score += 1

    def add_opponent(self):
        opponent = Opponent("assets/opponent_car.png")
        for existing_opponent in self.opponents:
            if opponent.rect.colliderect(existing_opponent.rect):
                return  # Não adiciona o oponente se ele colidir com um existente
        self.all_sprites.add(opponent)
        self.opponents.add(opponent)

    def draw(self):
        self.renderer.draw_background(self.road)
        self.renderer.draw_sprites(self.all_sprites)
        self.renderer.draw_text(f"Score: {self.score}", 10, 10)
        self.renderer.draw_text(f"High score: {self.high_score}", 10, 40)
        self.renderer.draw_text(f"Lives: {self.lives}", 10, 70)
        pygame.display.flip()
