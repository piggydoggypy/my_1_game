import pygame
import sys
import random
from tile import Tile, TileManager
from resources_loader import res_load
from map_render import render_noise
from hero import Hero
from camera import Camera

# Инициализация Pygame
pygame.init()

# Константы
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
FPS = 120

# Цвета
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

RESOURCES = {}


class Game:
    def __init__(self):
        global RESOURCES
        # Создание окна
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Моя 2D Игра")
        # Частота кадров
        self.clock = pygame.time.Clock()
        self.running = True
        # Загрузка ресурсов
        RESOURCES = res_load()
        # создание карты
        self.game_map = render_noise()
        self.hero = Hero(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, self.screen, SCREEN_WIDTH, SCREEN_HEIGHT)
        self.camera = Camera(self.hero, SCREEN_HEIGHT, SCREEN_WIDTH)
        self.clock.tick()
        # tilemanager
        self.tile_manager = TileManager(self.game_map, RESOURCES, self.screen, self.camera)
        # Инициализация игровых объектов
        self.init_game()

    def init_game(self):
        delta = self.clock.tick()
        """Инициализация игровых объектов"""

    def handle_events(self):
        """Обработка событий"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            # Клавиатура
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False

    def update(self, delta):
        """Обновление состояния игры"""

        # Обновление игрока
        self.hero.update(self.camera, delta)

    def draw(self):
        """Отрисовка игры"""
        # Очистка экрана
        self.screen.fill(BLACK)

        # Отрисовка карты

        self.tile_manager.output(0)

        # Отрисовка игровых объектов
        self.hero.output()

        # self.enemies.draw(self.screen)
        # self.projectiles.draw(self.screen)

        # Отрисовка интерфейса
        # self.draw_ui()

        # Обновление экрана
        pygame.display.flip()


    def run(self):
        """Главный игровой цикл"""
        while self.running:
            delta = self.clock.tick(FPS)
            self.handle_events()
            self.update(delta)
            self.draw()
            self.clock.tick(FPS)



        self.quit()

    def quit(self):
        """Корректный выход из игры"""
        pygame.quit()
        sys.exit()




def main():
    game = Game()
    game.run()


if __name__ == "__main__":
    main()
