# Generated by Django 3.0.7 on 2020-07-05 13:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0006_auto_20200705_1825'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tables',
            name='time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='waiting',
            name='add_time',
            field=models.TimeField(default=datetime.time(18, 35, 6, 632544)),
        ),
    ]