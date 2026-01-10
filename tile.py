import pygame

class Tile:
    def __init__(self, image, x, y) -> None:
        self.image = image
        self.x, self.y = x, y
        self.rect = pygame.Rect(x * 16, y * 16, 16, 16)

    def output(self, screen, rect) -> None:
        screen.blit(self.image, rect)

    def change_rect(self):
        pass



class TileManager:
    def __init__(self, game_map, resources, screen, camera) -> None:
        self.screen = screen
        self.resources = resources
        self.map = game_map
        self.camera = camera
        self.tiles = [[None for _ in range(len(game_map[0]))] for i in range(len(game_map))]
        self.init_tiles()

    def init_tiles(self) -> None:
        for i in range(len(self.map)):
            for j in range(len(self.map[0])):
                self.tiles[i][j] = Tile(self.determine_source(i, j), j, i)

    def determine_source(self, i, j) -> int:
        z = self.map[i][j]
        if z == -1:
            return self.resources['land'][0]
        else:
            return self.resources['water'][0]



    def output(self, player_perspective) -> None:
        # if in player_perspective !!!!!!!!!!
        for tiles in self.tiles:
            for tile in tiles:
                if self.camera.is_in_view(tile.rect):
                    tile.output(self.screen, self.camera.new_rect_for_tile(tile.x, tile.y))

