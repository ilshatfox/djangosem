# Generated by Django 2.2.12 on 2020-05-18 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proxies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proxy',
            name='ip',
            field=models.TextField(unique=True),
        ),
    ]
