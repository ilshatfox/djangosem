# Generated by Django 2.2.12 on 2020-05-18 10:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('proxies', '0001_initial'),
        ('vk_akk', '0002_vkakksgroup'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserAgent',
            fields=[
                ('id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('user_agent', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='vkakk',
            name='_cookies',
            field=models.TextField(default='{}'),
        ),
        migrations.AddField(
            model_name='vkakk',
            name='is_auth',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='vkakk',
            name='is_ban',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='vkakk',
            name='proxy',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='proxies.Proxy'),
        ),
        migrations.AddField(
            model_name='vkakk',
            name='user_agent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='vk_akk.UserAgent'),
        ),
    ]
