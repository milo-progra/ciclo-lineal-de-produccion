# Generated by Django 4.0.6 on 2022-08-02 14:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0041_alter_salida_id_area'),
    ]

    operations = [
        migrations.AlterField(
            model_name='oportunidades',
            name='id_area',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.areaempresa'),
        ),
    ]
