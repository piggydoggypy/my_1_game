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
SCREEN_HEIGHT = 1200
FPS = 60

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

        self.hero = Hero(SCREEN_WIDTH//2, SCREEN_HEIGHT//2, self.screen)

        self.camera = Camera(self.hero, SCREEN_HEIGHT, SCREEN_WIDTH)

        # tilemanager
        self.tile_manager = TileManager(self.game_map, RESOURCES, self.screen, self.camera)
        # Инициализация игровых объектов
        self.init_game()

    #

    def init_game(self):

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
                # elif event.key == pygame.K_SPACE:
                #     # Выстрел
                #     projectile = self.player.shoot()
                #     self.projectiles.add(projectile)

            # # Мышь
            # elif event.type == pygame.MOUSEBUTTONDOWN:
            #     if event.button == 1:  # Левая кнопка мыши
            #         # Действие по клику
            #         pass

    def update(self):
        """Обновление состояния игры"""
        pass
        # Обновление игрока
        self.hero.update(self.camera)
        # self.camera.update()

    #
    #         # Обновление врагов
    #         self.enemies.update()
    #
    #         # Обновление снарядов
    #         self.projectiles.update()
    #
    #         # Проверка столкновений
    #         self.check_collisions()
    #
    #         # Проверка условий уровня
    #         if len(self.enemies) == 0:
    #             self.level_up()
    #
    #     def check_collisions(self):
    #         """Проверка столкновений"""
    #         # Столкновения снарядов с врагами
    #         hits = pygame.sprite.groupcollide(self.projectiles, self.enemies, True, True)
    #         for hit in hits:
    #             self.score += 10
    #
    #         # Столкновение игрока с врагами
    #         if pygame.sprite.spritecollide(self.player, self.enemies, False):
    #             # Обработка повреждения игрока
    #             pass
    #
    #     def level_up(self):
    #         """Переход на следующий уровень"""
    #         self.level += 1
    #         # Создание новых врагов
    #         for i in range(5 + self.level * 2):
    #             enemy = Enemy(random.randint(0, SCREEN_WIDTH), random.randint(-100, -50))
    #             self.enemies.add(enemy)
    #
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

    #
    #     def draw_ui(self):
    #         """Отрисовка интерфейса"""
    #         # Счет
    #         score_text = self.font.render(f"Счет: {self.score}", True, WHITE)
    #         self.screen.blit(score_text, (10, 10))
    #
    #         # Уровень
    #         level_text = self.font.render(f"Уровень: {self.level}", True, WHITE)
    #         self.screen.blit(level_text, (10, 50))
    #
    #         # Здоровье игрока
    #         health_text = self.font.render(f"Здоровье: {self.player.health}", True, GREEN)
    #         self.screen.blit(health_text, (SCREEN_WIDTH - 200, 10))
    #
    def run(self):
        """Главный игровой цикл"""
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)

        self.quit()

    def quit(self):
        """Корректный выход из игры"""
        pygame.quit()
        sys.exit()


# class Player(pygame.sprite.Sprite):
#     def __init__(self, x, y):
#         super().__init__()
#         self.image = pygame.Surface((50, 50))
#         self.image.fill(BLUE)
#         self.rect = self.image.get_rect(center=(x, y))
#
#         # Характеристики игрока
#         self.speed = 5
#         self.health = 100
#         self.shoot_cooldown = 0
#
#     def update(self):
#         """Обновление состояния игрока"""
#         keys = pygame.key.get_pressed()
#
#         # Движение
#         if keys[pygame.K_LEFT] or keys[pygame.K_a]:
#             self.rect.x -= self.speed
#         if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
#             self.rect.x += self.speed
#         if keys[pygame.K_UP] or keys[pygame.K_w]:
#             self.rect.y -= self.speed
#         if keys[pygame.K_DOWN] or keys[pygame.K_s]:
#             self.rect.y += self.speed
#
#         # Ограничение движения в пределах экрана
#         self.rect.clamp_ip(pygame.Rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT))
#
#         # Обновление кулдауна стрельбы
#         if self.shoot_cooldown > 0:
#             self.shoot_cooldown -= 1
#
#     def shoot(self):
#         """Создание снаряда"""
#         if self.shoot_cooldown == 0:
#             self.shoot_cooldown = 10  # Кулдаун между выстрелами
#             return Projectile(self.rect.centerx, self.rect.top)
#         return None
#
#     def draw(self, screen):
#         """Отрисовка игрока"""
#         screen.blit(self.image, self.rect)
#
# class Enemy(pygame.sprite.Sprite):
#     def __init__(self, x, y):
#         super().__init__()
#         self.image = pygame.Surface((40, 40))
#         self.image.fill(RED)
#         self.rect = self.image.get_rect(center=(x, y))
#
#         # Характеристики врага
#         self.speed = random.randint(1, 3)
#
#     def update(self):
#         """Обновление врага"""
#         self.rect.y += self.speed
#
#         # Удаление врага, если он ушел за экран
#         if self.rect.top > SCREEN_HEIGHT:
#             self.kill()
#
# class Projectile(pygame.sprite.Sprite):
#     def __init__(self, x, y):
#         super().__init__()
#         self.image = pygame.Surface((5, 15))
#         self.image.fill(GREEN)
#         self.rect = self.image.get_rect(center=(x, y))
#
#         # Характеристики снаряда
#         self.speed = 10
#
#     def update(self):
#         """Обновление снаряда"""
#         self.rect.y -= self.speed
#
#         # Удаление снаряда, если он ушел за экран
#         if self.rect.bottom < 0:
#             self.kill()


def main():
    game = Game()
    game.run()


if __name__ == "__main__":
    main()
