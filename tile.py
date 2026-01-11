import pygame
from random import randint

AROUND = [[(-1, -1), (0, -1), (1, -1)],
          [(-1, 0), (0, 0), (1, 0)],
          [(-1, 1), (0, 1), (1, 1)],
          ]


class Tile:
    def __init__(self, image, x, y) -> None:
        self.image = image
        self.x, self.y = x, y
        self.is_water = False
        self.rect = pygame.Rect(x * 32, y * 32, 32, 32)

    def output(self, screen, rect) -> None:
        screen.blit(self.image, rect)

    def change_image(self, image):
        self.image = image

    def __str__(self):
        return f'Tile ({self.x},{self.y}) {"w" if self.is_water else "l"}'

    def __repr__(self):
        return f'Tile ({self.x},{self.y}) {"w" if self.is_water else "l"}'


class TileManager:
    def __init__(self, game_map, resources, screen, camera) -> None:
        self.screen = screen
        self.resources = resources
        self.map = game_map
        self.camera = camera
        self.tiles = [[None for _ in range(len(game_map[0]))] for i in range(len(game_map))]
        self.init_tiles()
        self.dilute_map()
        self.dilute_map()

    def init_tiles(self) -> None:
        for i in range(len(self.map)):
            for j in range(len(self.map[0])):
                self.tiles[i][j] = self.make_tile_source(i, j)

    def make_tile_source(self, i, j) -> Tile:
        z = abs(self.map[i][j])
        if z == 1:
            return Tile(self.resources['land'][0], j, i)
        else:
            tile = Tile(self.resources['water'][0], j, i)
            tile.is_water = True
            return tile

    def output(self, player_perspective) -> None:
        # if in player_perspective !!!!!!!!!!
        for tiles in self.tiles:
            for tile in tiles:
                if self.camera.is_in_view(tile.rect):
                    tile.output(self.screen, self.camera.new_rect_for_tile(tile.x, tile.y))

    def get_water_around(self, y0, x0):
        ans = [[None, None, None], [None, None, None], [None, None, None]]
        for i in range(3):
            for j in range(3):
                x, y = AROUND[i][j]
                if x0 + x in range(len(self.map[0])) and y0 + y in range(len(self.map)):
                    ans[i][j] = self.tiles[y0 + y][x0 + x].is_water

        return ans

    def dilute_water_tile(self, i, j):
        sp = self.get_water_around(i, j)
        count_water = 0
        for i in range(3):
            for j in range(3):
                if sp[i][j] or sp[i][j] is None:
                    count_water += 1

        if all(all(el for el in x) for x in sp):
            return self.resources['water'][randint(0, 1)]
        elif count_water >= 4:
            if (sp[1][0] is False) and (sp[0][1] is False) and (sp[1][2] is False):
                self.tiles[i][j].is_water = False
                return self.resources['land'][0]
            elif (sp[1][0] is False) and (sp[0][1] is False) and (sp[2][1] is False):
                self.tiles[i][j].is_water = False
                return self.resources['land'][0]
            elif (sp[0][1] is False) and (sp[2][1] is False) and (sp[1][2] is False):
                self.tiles[i][j].is_water = False
                return self.resources['land'][0]
            elif (sp[2][1] is False) and (sp[1][0] is False) and (sp[1][2] is False):
                self.tiles[i][j].is_water = False
                return self.resources['land'][0]

            elif (sp[2][2] is False) and (sp[2][1] is False) and (sp[1][2] is False):
                return self.resources['water'][12]
            elif (sp[2][0] is False) and (sp[2][1] is False) and (sp[1][0] is False):
                return self.resources['water'][10]
            elif (sp[0][2] is False) and (sp[0][1] is False) and (sp[1][2] is False):
                return self.resources['water'][11]
            elif (sp[0][0] is False) and (sp[0][1] is False) and (sp[1][0] is False):
                return self.resources['water'][13]

            elif sp[2][1] is False:
                return self.resources['water'][6]
            elif sp[1][0] is False:
                return self.resources['water'][9]
            elif sp[0][1] is False:
                return self.resources['water'][7]
            elif sp[1][2] is False:
                return self.resources['water'][8]

            elif sp[2][2] is False:
                return self.resources['water'][3]
            elif sp[0][0] is False:
                return self.resources['water'][4]
            elif sp[0][2] is False:
                return self.resources['water'][5]
            elif sp[2][0] is False:
                return self.resources['water'][2]

            else:
                return self.resources['water'][0]
        else:
            return self.resources['water'][0]

    def dilute_map(self) -> None:
        for i in range(len(self.map)):
            for j in range(len(self.map[0])):
                if self.tiles[i][j].is_water:
                    self.tiles[i][j].change_image(self.dilute_water_tile(i, j))
                else:
                    self.tiles[i][j].change_image(self.resources['land'][randint(0, 1)])

