# Generated by Django 4.0.6 on 2022-07-20 13:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_rename_carta_nota'),
    ]

    operations = [
        migrations.RenameField(
            model_name='nota',
            old_name='id_Carta',
            new_name='id_nota',
        ),
    ]
