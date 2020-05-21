# Generated by Django 2.2.12 on 2020-05-15 23:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('vk_akk', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='VkAkksGroup',
            fields=[
                ('id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('vk_akks', models.ManyToManyField(to='vk_akk.VkAkk')),
            ],
        ),
    ]
