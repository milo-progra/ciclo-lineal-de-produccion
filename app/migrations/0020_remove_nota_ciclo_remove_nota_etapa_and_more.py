# Generated by Django 4.0.6 on 2022-07-20 18:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0019_rename_id_etapa_oportunidades_etapa_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nota',
            name='ciclo',
        ),
        migrations.RemoveField(
            model_name='nota',
            name='etapa',
        ),
        migrations.RemoveField(
            model_name='nota',
            name='opcion',
        ),
        migrations.RemoveField(
            model_name='nota',
            name='usuario',
        ),
        migrations.RemoveField(
            model_name='oportunidades',
            name='cicloArea',
        ),
        migrations.RemoveField(
            model_name='oportunidades',
            name='etapa',
        ),
        migrations.RemoveField(
            model_name='oportunidades',
            name='usuario',
        ),
        migrations.RemoveField(
            model_name='salida',
            name='cicloArea',
        ),
        migrations.RemoveField(
            model_name='salida',
            name='etapa',
        ),
        migrations.RemoveField(
            model_name='salida',
            name='usuario',
        ),
        migrations.DeleteModel(
            name='Entrada',
        ),
        migrations.DeleteModel(
            name='Nota',
        ),
        migrations.DeleteModel(
            name='Oportunidades',
        ),
        migrations.DeleteModel(
            name='Salida',
        ),
    ]
