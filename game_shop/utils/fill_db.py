import os
import django
import json
from django.core.files import File


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "game_shop.settings")
django.setup()

from shop_app.models import Game, Genre


def read_data():
    with open('data.json', 'r', encoding='utf-8') as file:
        load_data = json.load(file)
    
    return load_data


games_data = read_data()

def fill():

    for game_data in games_data:
        genre_names = game_data.get("Жанр", "").split(", ")

        # Создаем или получаем жанры
        genres = []
        for genre_name in genre_names:
            genre, created = Genre.objects.get_or_create(name=genre_name.strip())
            genres.append(genre)

        try:
            game, created = Game.objects.get_or_create(
                path=game_data["img"],
                title=game_data["title"],
                price=game_data["price"],
                date_of_release=game_data["date_of_release"],
                game_description=game_data["game_description"],
                platform=game_data["Платформа"],
                os_requirements=game_data["Операционная система"],
                processor_requirements=game_data["Процессор"],
                memory_requirements=game_data["Оперативная память"],
                graphics_card_requirements=game_data["Видеокарта"],
                disk_space_requirements=game_data["Свободное место на жестком диске"],
            )
        except:
            continue

        if created:
            print(f"Created new game: {game.title}")

        game.genre.set(genres)

if __name__ == "__main__":
    fill()