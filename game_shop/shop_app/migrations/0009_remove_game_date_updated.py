# Generated by Django 4.2.4 on 2023-09-30 17:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop_app', '0008_remove_game_genre_game_genre'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='date_updated',
        ),
    ]
