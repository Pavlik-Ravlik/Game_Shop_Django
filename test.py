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
