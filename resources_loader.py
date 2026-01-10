import sys
import os
import pygame

BASE_PATH = "files/tiles"

RESOURCES = {
    'water': [
        "water_1",
        "water_2",
        "water_3",
        "water_cornerland_down-left",
        "water_cornerland_down-right",
        "water_cornerland_up-left",
        "water_cornerland_up-right",
        "water_land_down",
        "water_land_up",
        "water_land_right",
        "water_land_left",
        "water_land_down-left",
        "water_land_up-right",
        "water_cornerland_down-right",
        "water_land_up-left"
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
                # print(f"Загружен: {filepath}")

    except Exception as e:
        print(f'Ошибка загрузки файлов: {e}')
        sys.exit()

    return loaded_resources


if __name__ == "__main__":
    resources = res_load()
