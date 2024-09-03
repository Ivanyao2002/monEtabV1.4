# Generated by Django 5.1 on 2024-09-03 03:45

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('base', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TeacherModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Date de création ')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name="Date d'édition ")),
                ('status', models.BooleanField(default=True, verbose_name='Status ')),
                ('first_name', models.CharField(max_length=30, verbose_name='Nom ')),
                ('last_name', models.CharField(max_length=60, verbose_name='Prénoms ')),
                ('gender', models.CharField(choices=[('H', 'Homme'), ('F', 'Femme'), ('O', 'Autre')], default='H', max_length=1, verbose_name='Genre ')),
                ('birthday', models.DateField(verbose_name='Date de naissance ')),
                ('phone_number', models.CharField(max_length=15, verbose_name='Téléphone ')),
                ('url_picture', models.CharField(max_length=255, verbose_name="Lien de l'image ")),
                ('active', models.BooleanField(default=False, verbose_name='Actif ')),
                ('available', models.BooleanField(default=True, verbose_name='Disponible ')),
                ('speciality', models.CharField(max_length=50, verbose_name='Spécialité ')),
                ('address', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.adressmodel')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Professeur',
                'verbose_name_plural': 'Professeurs',
            },
        ),
    ]
