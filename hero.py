import os
import pygame


class Hero:
    def __init__(self, x, y, screen, width, height):
        self.width, self.height = width, height
        self.image = None
        self.load_res()
        self.size = 32
        self.rect = pygame.Rect(x, y, self.size, self.size)
        # self.speed = 1000
        self.speed = 5000
        self.screen = screen

    def load_res(self):
        filepath = os.path.join(r'files/hero', f"tile000.png")
        self.image = pygame.image.load(filepath)

    def output(self):
        self.screen.blit(self.image,
                         pygame.Rect(self.width // 2 - self.size // 2, self.height // 2 - self.size // 2, self.size,
                                     self.size))

    def update(self, camera, delta):
        """Обновление состояния игрока"""
        keys = pygame.key.get_pressed()

        # Движение
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.rect.x -= self.speed * (delta / 1000)
            camera.rect.x -= self.speed * (delta / 1000)


        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rect.x += self.speed * (delta / 1000)
            camera.rect.x += self.speed * (delta / 1000)


        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.rect.y -= self.speed * (delta / 1000)
            camera.rect.y -= self.speed * (delta / 1000)


        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            camera.rect.y += self.speed * (delta / 1000)
            self.rect.y += self.speed * (delta / 1000)