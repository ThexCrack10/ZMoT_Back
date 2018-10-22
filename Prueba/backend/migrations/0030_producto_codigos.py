# Generated by Django 2.1.2 on 2018-10-19 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0029_remove_producto_codigos'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='codigos',
            field=models.ManyToManyField(through='backend.CodigoProducto', to='backend.TipoCodigo'),
        ),
    ]