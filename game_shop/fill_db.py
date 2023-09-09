import os
import django
import json
from django.core.files import File

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "game_shop.settings")
django.setup()

from shop_app.models import Game



def read_data():
    with open('data.json', 'r', encoding='utf-8') as file:
        load_data = json.load(file)
    
    return load_data


games_data = read_data()



def fill():
    for games in games_data:
        Game.objects.get_or_create(
            path=games.get('img'),
            title=games.get("title"),
            price=games.get("price"),
            date_of_release=games.get("date_of_release"),
            game_description=games.get("game_description"),
            genre=games.get("Жанр"),
            platform=games.get("Платформа"),
            os_requirements=games.get("Операционная система"),
            processor_requirements=games.get("Процессор"),
            memory_requirements=games.get("Оперативная память"),
            graphics_card_requirements=games.get("Видеокарта"),
            disk_space_requirements=games.get("Свободное место на жестком диске"),
        )


if __name__ == '__main__':
    fill()