# Generated by Django 4.2.4 on 2023-08-29 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_app', '0004_alter_game_platform'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='date_of_release',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='date_updated',
            field=models.CharField(max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='disk_space_requirements',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='game_description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='graphics_card_requirements',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='memory_requirements',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='os_requirements',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='price',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='processor_requirements',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='title',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
