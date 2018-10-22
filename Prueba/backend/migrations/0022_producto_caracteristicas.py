# Generated by Django 2.1.1 on 2018-10-17 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0021_auto_20181016_2314'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='caracteristicas',
            field=models.ManyToManyField(blank=True, through='backend.CaracteristicaProducto', to='backend.Caracteristica'),
        ),
    ]
