# Generated by Django 5.1 on 2024-09-19 07:07

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='baseuser',
            name='id',
        ),
        migrations.RemoveField(
            model_name='baseuser',
            name='uid',
        ),
        migrations.AddField(
            model_name='baseuser',
            name='userid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
