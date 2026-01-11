import os
os.environ['TK_LIBRARY'] = 'C:/Users/piggydoggy/AppData/Local/Programs/Python/Python313/tcl/tcl8.6'
os.environ['TCL_LIBRARY'] = 'C:/Users/piggydoggy/AppData/Local/Programs/Python/Python313/tcl/tcl8.6'
from numpy import floor
from perlin_noise import PerlinNoise
import matplotlib.pyplot as plt
from random import randrange




def render_noise() -> list:
            ### генерация основного шума и параметризация ###

    noise = PerlinNoise(octaves=2, seed=randrange(1000, 9999)) # рандомный сид
    # noise = PerlinNoise(octaves=2, seed=2048)
    amp = 1 # отвечает за высоту(за биомы)
    period = 75 # чем больше, тем более гладкий шум
    terrain_width = 300

    #генерация матрицы для представления ландшафта
    landscale = [[0 for i in range(terrain_width)] for i in range(terrain_width)]


    for position in range(terrain_width**2):
        x = floor(position / terrain_width)
        z = floor(position % terrain_width)
        y = floor(noise([x/period, z/period])*amp)
        landscale[int(x)][int(z)] = int(y)
        # print(int(y))

    # plt.imshow(landscale)
    # plt.show()
    return  landscale


def main():
    render_noise()


if __name__ == "__main__":
    main()
