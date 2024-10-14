# Generated by Django 5.1 on 2024-10-08 09:34

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0032_movie_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='movie_uid',
            field=models.UUIDField(default=uuid.uuid4),
        ),
    ]
