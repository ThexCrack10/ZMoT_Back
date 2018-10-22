# Generated by Django 2.1.2 on 2018-10-20 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0032_producto_medidas'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='caracteristicas',
            field=models.ManyToManyField(blank=True, through='backend.CaracteristicaProducto', to='backend.Caracteristica'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='codigos',
            field=models.ManyToManyField(blank=True, through='backend.CodigoProducto', to='backend.TipoCodigo'),
        ),
    ]