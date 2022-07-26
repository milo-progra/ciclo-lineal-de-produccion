# Generated by Django 4.0.6 on 2022-07-20 19:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0020_remove_nota_ciclo_remove_nota_etapa_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entrada',
            fields=[
                ('id_entrada', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('fecha', models.DateField()),
                ('cicloArea', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.cicloarea')),
                ('etapa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.etapa')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
