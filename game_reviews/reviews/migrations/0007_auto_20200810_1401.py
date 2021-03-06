# Generated by Django 3.1 on 2020-08-10 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0006_auto_20200810_1345'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='author',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='review',
            name='image',
            field=models.ImageField(blank=True, max_length=255, null=True, upload_to='reviews/review_images/'),
        ),
        migrations.AddField(
            model_name='review',
            name='long_quote',
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='review',
            name='review_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='review',
            name='review_url',
            field=models.URLField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='review',
            name='score',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='review',
            name='short_quote',
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='review',
            name='show_logo_img',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='reviewsite',
            name='max_score',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='reviewsite',
            name='logo_img',
            field=models.ImageField(blank=True, max_length=255, null=True, upload_to='review_sites/logo_images/'),
        ),
        migrations.AlterField(
            model_name='reviewsite',
            name='site_url',
            field=models.URLField(blank=True, max_length=255, null=True),
        ),
    ]
