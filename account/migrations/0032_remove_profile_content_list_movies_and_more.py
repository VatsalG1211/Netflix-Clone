# Generated by Django 5.1 on 2024-09-27 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0031_alter_content_c_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile_content_list',
            name='movies',
        ),
        migrations.RemoveField(
            model_name='profile_content_list',
            name='seasons',
        ),
        migrations.AddField(
            model_name='profile_content_list',
            name='content',
            field=models.ManyToManyField(to='account.content'),
        ),
    ]
