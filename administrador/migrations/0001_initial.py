# Generated by Django 4.0.6 on 2022-09-01 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LogTelegram',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timesstap', models.DateField(auto_now_add=True)),
                ('text', models.CharField(max_length=100)),
            ],
        ),
    ]
