# Generated by Django 4.1.1 on 2022-09-30 02:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Transporte', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehiculo',
            name='propietario',
            field=models.ForeignKey(max_length=20, on_delete=django.db.models.deletion.CASCADE, to='Transporte.propietario', verbose_name='Nombre del propietario'),
        ),
    ]