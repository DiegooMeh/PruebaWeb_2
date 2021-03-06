# Generated by Django 2.2.17 on 2020-12-07 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Casas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('baths', models.IntegerField(default=1)),
                ('metros', models.IntegerField()),
                ('foto', models.ImageField(upload_to='casas')),
                ('materiales', models.CharField(max_length=70)),
                ('estilo', models.CharField(max_length=70)),
                ('precio', models.IntegerField()),
                ('habitaciones', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('correo', models.CharField(max_length=40)),
                ('apellido', models.CharField(max_length=40)),
                ('numero', models.CharField(max_length=9)),
            ],
        ),
    ]
