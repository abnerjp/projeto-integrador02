# Generated by Django 4.0.5 on 2022-06-19 00:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barbershop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='servico',
            name='tempo_estimado',
            field=models.TimeField(default=datetime.time(0, 30)),
        ),
    ]
