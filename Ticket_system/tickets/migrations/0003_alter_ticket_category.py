# Generated by Django 4.2.7 on 2024-04-26 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0002_alter_ticket_creation_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='category',
            field=models.CharField(choices=[('Technical', 'Technical'), ('Billing', 'Billing'), ('Service', 'Service')], default='Technical', max_length=20),
        ),
    ]