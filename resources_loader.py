import sys
import os
import pygame

BASE_PATH = "files/tiles"

RESOURCES = {
    'water': [
        "water_1",#0
        "water_2",#1
        "water_cornerland_down-left",#2
        "water_cornerland_down-right",#3
        "water_cornerland_up-left",#4
        "water_cornerland_up-right",#5
        "water_land_down",#6
        "water_land_up",#7
        "water_land_right",#8
        "water_land_left",#9
        "water_land_down-left",#10
        "water_land_up-right",#11
        "water_land_down-right",#12
        "water_land_up-left"#13
    ],
    'land': [
        "grass_1",
        "grass_2",
        "dirt_1",
        "dirt_2"
    ]
}

def res_load() -> dict:
    """Загружает все ресурсы из RESOURCES"""
    loaded_resources = {}

    try:
        for category, filenames in RESOURCES.items():
            loaded_resources[category] = []

            for filename in filenames:
                # Формируем полный путь к файлу

                filepath = os.path.join(BASE_PATH, f'{category}', f"{filename}.png")

                # Загружаем изображение
                image = pygame.image.load(filepath)
                loaded_resources[category].append(image)
                print(f"Загружен: {filepath}")

    except Exception as e:
        print(f'Ошибка загрузки файлов: {e}')
        sys.exit()

    return loaded_resources


if __name__ == "__main__":
    resources = res_load()
