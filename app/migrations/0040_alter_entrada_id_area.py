# Generated by Django 4.0.6 on 2022-08-01 16:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0039_remove_entrada_id_empresa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entrada',
            name='id_area',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.areaempresa'),
        ),
    ]
