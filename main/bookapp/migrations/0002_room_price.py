# Generated by Django 5.0.6 on 2024-07-19 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='price',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=6),
        ),
    ]
