# Generated by Django 4.2.4 on 2023-10-01 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_app', '0009_remove_game_date_updated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='title',
            field=models.CharField(max_length=255, null=True, unique=True),
        ),
    ]