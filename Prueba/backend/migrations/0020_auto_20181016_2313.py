# Generated by Django 2.1.1 on 2018-10-17 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0019_auto_20181016_2308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='codigoproducto',
            name='valor',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='tipocodigo',
            name='nombre',
            field=models.CharField(max_length=128),
        ),
    ]
