# Generated by Django 4.2.5 on 2023-10-12 12:37

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('postres', '0003_remove_tipodepostre_categoria_delete_postre_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='postres',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.CharField(blank=True, max_length=250, null=True, verbose_name='descripcion')),
            ],
        ),
        migrations.CreateModel(
            name='tiposdepostres',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('cantidad', models.FloatField()),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('descripcion', models.CharField(blank=True, max_length=250, null=True, verbose_name='descripción')),
                ('fecha_actualizacion', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='fecha de actualización')),
                ('categoria', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='postres.postres', verbose_name='categoría')),
            ],
            options={
                'verbose_name': 'tipo de postre',
                'verbose_name_plural': 'tipos de postres',
            },
        ),
    ]
