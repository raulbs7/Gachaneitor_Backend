# Generated by Django 3.1.3 on 2021-01-10 10:45

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Receta',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=128)),
                ('descripcion', models.TextField()),
                ('tmp_preparacion', models.IntegerField(default=0)),
                ('ud_tmp_preparacion', models.CharField(choices=[('h', 'Horas'), ('min', 'Minutos'), ('s', 'Segundos')], max_length=3)),
                ('tmp_total', models.IntegerField(default=0)),
                ('ud_tmp_total', models.CharField(choices=[('h', 'Horas'), ('min', 'Minutos'), ('s', 'Segundos')], max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Paso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_paso', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('verbo', models.CharField(max_length=128)),
                ('tipo_verbo', models.CharField(choices=[('cocinar', 'Cocinar'), ('persona', 'Por la persona'), ('mover', 'Mover')], max_length=64)),
                ('ingredientes', models.TextField()),
                ('temperatura', models.IntegerField(blank=True, null=True)),
                ('ud_temperatura', models.CharField(blank=True, choices=[('ºC', 'Grados centígrados'), ('ºF', 'Grados farenheit')], max_length=2)),
                ('velocidad', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(9)])),
                ('tiempo', models.IntegerField(blank=True, null=True)),
                ('ud_tiempo', models.CharField(blank=True, choices=[('h', 'Horas'), ('min', 'Minutos'), ('s', 'Segundos')], max_length=3)),
                ('receta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.receta')),
            ],
            options={
                'unique_together': {('receta', 'num_paso')},
            },
        ),
        migrations.CreateModel(
            name='Ingrediente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=128)),
                ('cantidad', models.IntegerField(default=0)),
                ('ud_cantidad', models.CharField(choices=[('ud', 'Unidades'), ('mg', 'Miligramos'), ('g', 'Gramos'), ('kg', 'Kilogramos'), ('ml', 'Mililitros'), ('l', 'Litros')], max_length=2)),
                ('receta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.receta')),
            ],
            options={
                'unique_together': {('receta', 'nombre')},
            },
        ),
    ]
