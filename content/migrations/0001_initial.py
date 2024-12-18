# Generated by Django 5.1 on 2024-09-23 10:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0017_alter_profile_choice'),
    ]

    operations = [
        migrations.CreateModel(
            name='Series',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('no_of_season', models.IntegerField(default=0)),
                ('is_adult', models.BooleanField(default=True)),
                ('title_img', models.ImageField(upload_to='media/movie/title_img')),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('poster', models.ImageField(upload_to='media/movie/poster')),
                ('banner_img', models.ImageField(upload_to='media/movie/banner')),
                ('title_img', models.ImageField(upload_to='media/movie/title_img')),
                ('is_adult', models.BooleanField(default=True)),
                ('upload_trailer', models.CharField(max_length=500)),
                ('upload_movie', models.CharField(max_length=500)),
                ('released_date', models.DateField(auto_now_add=True)),
                ('likes', models.IntegerField(default=0)),
                ('actors', models.ManyToManyField(to='account.actor')),
                ('genres', models.ManyToManyField(to='account.genre')),
            ],
        ),
        migrations.CreateModel(
            name='Season',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('season_no', models.IntegerField(default=1)),
                ('poster', models.ImageField(upload_to='media/movie/poster')),
                ('banner_img', models.ImageField(upload_to='media/movie/banner')),
                ('upload_trailer', models.CharField(max_length=500)),
                ('released_date', models.DateField(auto_now_add=True)),
                ('likes', models.IntegerField(default=0)),
                ('actors', models.ManyToManyField(to='account.actor')),
                ('genres', models.ManyToManyField(to='account.genre')),
                ('series', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='season', to='content.series')),
            ],
        ),
        migrations.CreateModel(
            name='Episode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('episode_no', models.IntegerField(default=1)),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=300)),
                ('thumbnail', models.ImageField(upload_to='media/movie/thumbnail')),
                ('upload_episode', models.CharField(max_length=500)),
                ('released_date', models.DateField(auto_now_add=True)),
                ('season', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='episode', to='content.season')),
            ],
        ),
    ]
