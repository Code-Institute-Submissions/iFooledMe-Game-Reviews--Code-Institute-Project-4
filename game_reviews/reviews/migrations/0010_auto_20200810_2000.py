# Generated by Django 3.1 on 2020-08-10 20:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0009_auto_20200810_1957'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='game_id',
            new_name='game',
        ),
    ]
