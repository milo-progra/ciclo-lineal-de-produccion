# Generated by Django 4.0.6 on 2022-07-25 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0032_remove_entrada_cicloarea'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entrada',
            name='fecha',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
