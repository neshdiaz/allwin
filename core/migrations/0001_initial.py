# Generated by Django 2.2 on 2019-06-07 01:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Juego',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('posicion', models.SmallIntegerField(default=-1)),
                ('posicion_cerrado', models.SmallIntegerField(default=-1)),
                ('color_cerrado', models.CharField(default='red', max_length=10)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Juegos',
                'ordering': ['created'],
            },
        ),
        migrations.CreateModel(
            name='Jugador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('n_referidos', models.SmallIntegerField(default=0)),
                ('n_referidos_activados', models.SmallIntegerField(default=0)),
                ('color', models.CharField(default='red', max_length=10)),
                ('ciclo', models.BigIntegerField(default=0)),
                ('patrocinador', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Jugador')),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Jugadores',
            },
        ),
        migrations.CreateModel(
            name='Nivel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('indice', models.SmallIntegerField(blank=True, default=1, unique=True)),
                ('monto', models.DecimalField(decimal_places=2, default=50000, max_digits=10)),
            ],
            options={
                'verbose_name_plural': 'Niveles',
            },
        ),
        migrations.CreateModel(
            name='Lista',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alias', models.CharField(blank=True, default='', max_length=20, null=True)),
                ('max_items', models.SmallIntegerField(default=7)),
                ('items', models.SmallIntegerField(default=0)),
                ('cycle_position', models.SmallIntegerField(default=6)),
                ('ciclo', models.BigIntegerField(default=0)),
                ('tipo', models.CharField(choices=[('P', 'Principal'), ('S1', 'Sublista Izq'), ('S2', 'Sublista Ciclaje')], max_length=2)),
                ('estado', models.CharField(choices=[('A', 'ABIERTA'), ('C', 'CERRADA'), ('B', 'BLOQUEADA')], default='A', max_length=1)),
                ('pc', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('jugador', models.ManyToManyField(blank=True, default='', through='core.Juego', to='core.Jugador')),
                ('lista_padre', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Lista')),
                ('nivel', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.Nivel')),
            ],
            options={
                'verbose_name_plural': 'Listas',
                'ordering': ['created'],
            },
        ),
        migrations.AddField(
            model_name='juego',
            name='jugador',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Jugador'),
        ),
        migrations.AddField(
            model_name='juego',
            name='lista',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Lista'),
        ),
        migrations.CreateModel(
            name='Clon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.CharField(choices=[('P', 'PENDIENTE ACTIVAR'), ('A', 'ACTIVO')], default='P', max_length=1)),
                ('jugador', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Jugador')),
                ('nivel', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.Nivel')),
            ],
            options={
                'verbose_name_plural': 'Clones',
            },
        ),
    ]
