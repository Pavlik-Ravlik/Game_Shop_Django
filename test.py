from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Game(models.Model):
    path = models.ImageField(upload_to='uploads/', default='')
    title = models.CharField(max_length=255, null=True)
    price = models.PositiveIntegerField(null=True)
    date_of_release = models.DateField(null=True)
    game_description = models.TextField(null=True)
    date_updated = models.CharField(max_length=4, null=True)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, null=True)
    platform = models.CharField(max_length=50, null=True)
    os_requirements = models.TextField(null=True)
    processor_requirements = models.CharField(max_length=255, null=True)
    memory_requirements = models.CharField(max_length=255, null=True)
    graphics_card_requirements = models.CharField(max_length=255, null=True)
    disk_space_requirements = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.title
    


# Импортируйте модели
from your_app.models import Game, Genre

# Данные из вашего объекта
data = {
    "img": "uploads/Калибр (Caliber).jpg",
    "title": "Калибр (Caliber)",
    "price": 100,
    "date_of_release": "2023-06-18",
    "game_description": "...",
    "Жанр": "Action, MMOFPS, Симулятор, Shooter, Online",
    # Другие поля...
}

# Разделите жанры
genre_names = data["Жанр"].split(", ")

# Попробуйте найти существующие жанры или создать новые
genres = []
for genre_name in genre_names:
    genre, created = Genre.objects.get_or_create(name=genre_name)
    genres.append(genre)

# Создайте или обновите запись Game
game, created = Game.objects.get_or_create(
    title=data["title"],
    defaults={
        "path": data["img"],
        "price": data["price"],
        "date_of_release": data["date_of_release"],
        "game_description": data["game_description"],
        # Другие поля...
    }
)

# Установите связи с жанрами
game.genre.set(genres)

# Выведите информацию о созданной или обновленной игре
if created:
    print(f"Создана новая игра: {game.title}")
else:
    print(f"Игра обновлена: {game.title}")
