# Generated by Django 4.0.5 on 2022-07-24 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCC', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='presupuesto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('telefono', models.IntegerField()),
                ('mail', models.EmailField(max_length=254)),
                ('pedido', models.CharField(max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='productomay',
        ),
        migrations.DeleteModel(
            name='productomin',
        ),
        migrations.DeleteModel(
            name='Tramos',
        ),
    ]
