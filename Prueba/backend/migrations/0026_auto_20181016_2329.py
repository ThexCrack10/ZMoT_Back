# Generated by Django 2.1.1 on 2018-10-17 02:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0025_producto_medidas'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='codigos',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='medidas',
        ),
    ]
