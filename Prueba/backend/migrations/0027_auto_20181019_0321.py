# Generated by Django 2.1.2 on 2018-10-19 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0026_auto_20181016_2329'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='codigos',
            field=models.ManyToManyField(blank=True, through='backend.CodigoProducto', to='backend.TipoCodigo'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='caracteristicas',
            field=models.ManyToManyField(through='backend.CaracteristicaProducto', to='backend.Caracteristica'),
        ),
    ]