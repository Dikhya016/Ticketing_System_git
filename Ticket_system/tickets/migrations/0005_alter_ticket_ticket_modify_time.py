# Generated by Django 4.2.7 on 2024-05-03 04:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0004_ticket_ticket_modify_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='ticket_modify_time',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 3, 15, 26, 24, 107100)),
        ),
    ]