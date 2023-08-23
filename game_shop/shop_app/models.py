from django.db import models
from PIL import Image

class Game(models.Model):
    name = models.CharField(max_length=50, unique=True)
    price = models.IntegerField()
    game_description = models.CharField(max_length=500)
    date_of_release = models.DateTimeField()
    image = models.ImageField(upload_to='images/')
    category = models.CharField(max_length=15, null=False)
    
    def __str__(self):
        return self.name

class SystemRequirements(models.Model):
    operating_system = models.CharField(max_length=30)
    CPU = models.CharField(max_length=20)
    RAM = models.CharField(max_length=10)
    video_card = models.CharField(max_length=20)
    free_space = models.CharField(max_length=25)
    game = models.OneToOneField(Game, on_delete=models.CASCADE, null=False)
    
    def __str__(self):
        return self.game.name
