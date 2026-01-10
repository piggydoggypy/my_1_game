import os
import pygame


class Hero:
    def __init__(self, x, y, screen):
        self.image = None
        self.load_res()
        self.rect = pygame.Rect(x, y, 16, 16)
        self.speed = 5
        self.screen = screen

    def load_res(self):
        filepath = os.path.join(r'files/hero', f"tile000.png")
        self.image = pygame.image.load(filepath)


    def output(self):
        self.screen.blit(self.image, self.rect)

    def update(self, camera):
        """Обновление состояния игрока"""
        keys = pygame.key.get_pressed()

        # Движение
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.rect.x -= self.speed
            camera.rect.x -= self.speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rect.x += self.speed
            camera.rect.x += self.speed

        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.rect.y -= self.speed
            camera.rect.y -= self.speed

        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            camera.rect.y += self.speed
            self.rect.y += self.speed