# Generated by Django 4.1.2 on 2022-11-02 20:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_rename_compra_producto_compra'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='Compra',
        ),
    ]
