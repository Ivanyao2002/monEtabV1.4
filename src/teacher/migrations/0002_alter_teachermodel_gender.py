# Generated by Django 5.1 on 2024-09-07 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teachermodel',
            name='gender',
            field=models.CharField(choices=[('Homme', 'Homme'), ('Femme', 'Femme'), ('Autre', 'Autre')], default='Homme', max_length=10, verbose_name='Genre '),
        ),
    ]
