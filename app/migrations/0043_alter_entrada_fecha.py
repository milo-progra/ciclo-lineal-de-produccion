# Generated by Django 4.0.6 on 2022-08-11 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0042_alter_oportunidades_id_area'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entrada',
            name='fecha',
            field=models.DateField(auto_now_add=True),
        ),
    ]
