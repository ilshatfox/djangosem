# Generated by Django 2.2.12 on 2020-05-15 23:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('vk_akk', '0002_vkakksgroup'),
        ('vk_users', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AkkFollowTask',
            fields=[
                ('id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('complete_num', models.IntegerField(default=0)),
                ('success_num', models.IntegerField(default=0)),
                ('vk_akk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vk_akk.VkAkk')),
                ('vk_users', models.ManyToManyField(to='vk_users.VkUser')),
            ],
        ),
        migrations.CreateModel(
            name='ActionTask',
            fields=[
                ('id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('task_type', models.TextField(choices=[('ADD_FRIEND', 'ADD_FRIEND')])),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
