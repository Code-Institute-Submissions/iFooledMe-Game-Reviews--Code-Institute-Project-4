# Generated by Django 3.1 on 2020-08-06 12:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0007_platform_icon'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='tags',
        ),
        migrations.RemoveField(
            model_name='platform',
            name='icon',
        ),
        migrations.RemoveField(
            model_name='tag',
            name='tag_category',
        ),
    ]
