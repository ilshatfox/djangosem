# Generated by Django 2.2.12 on 2020-05-20 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vk_users', '0004_vkfileusers'),
    ]

    operations = [
        migrations.AddField(
            model_name='vkfileusers',
            name='filename',
            field=models.TextField(default='fff'),
        ),
    ]
