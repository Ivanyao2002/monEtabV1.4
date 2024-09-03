# Generated by Django 5.1 on 2024-09-03 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdressModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Date de création ')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name="Date d'édition ")),
                ('status', models.BooleanField(default=True, verbose_name='Status ')),
                ('city', models.CharField(max_length=50, verbose_name='Ville ')),
                ('street', models.CharField(max_length=50, verbose_name='Quartier ')),
                ('country', models.CharField(max_length=50, verbose_name='Pays ')),
            ],
            options={
                'verbose_name': 'Adresse',
                'verbose_name_plural': 'Adresses',
            },
        ),
    ]