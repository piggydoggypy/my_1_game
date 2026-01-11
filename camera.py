import pygame

class Camera:
    def __init__(self, hero, height, width):
        self.hero = hero
        self.height, self.width = height, width
        self.rect = pygame.Rect(self.hero.rect.x - width // 2, self.hero.rect.y - height // 2,width, height)

    # def update(self):
    #     self.rect = pygame.Rect(self.hero.rect.x - self.width // 2, self.hero.rect.y - self.height // 2,
    #                             self.width, self.height)

    def is_in_view(self, rect) -> bool:
        return abs(rect.x - self.hero.rect.x) <= self.width and abs(rect.y - self.hero.rect.y) <= self.height

    def new_rect_for_tile(self,x, y) -> pygame.Rect:
        return pygame.Rect(x*32 - self.hero.rect.x, y*32 - self.hero.rect.y, 32, 32)


    # def new_coors(self):