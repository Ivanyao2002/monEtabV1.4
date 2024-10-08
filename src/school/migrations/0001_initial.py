# Generated by Django 5.1 on 2024-08-31 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AbsenceModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
                ('absence_date', models.DateField(verbose_name="Date de l'absence")),
                ('absence_number', models.IntegerField(verbose_name="Nombre d'absence")),
            ],
            options={
                'verbose_name': 'Absence',
                'verbose_name_plural': 'Absences',
            },
        ),
        migrations.CreateModel(
            name='SchoolModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=180)),
                ('url_logo', models.CharField(max_length=50, verbose_name='Lien du logo')),
            ],
            options={
                'verbose_name': 'Ecole',
                'verbose_name_plural': 'Ecoles',
            },
        ),
        migrations.CreateModel(
            name='StudentCardsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
                ('issue_date', models.DateField(verbose_name="Date d'issue'")),
                ('reference', models.CharField(max_length=50, verbose_name='Référence')),
                ('expiration_date', models.DateField(verbose_name="Date d'expiration'")),
            ],
            options={
                'verbose_name': 'Carte Etudiant',
                'verbose_name_plural': 'Cartes Etudiant',
            },
        ),
        migrations.CreateModel(
            name='StudentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
                ('first_name', models.CharField(max_length=30, verbose_name='Nom')),
                ('last_name', models.CharField(max_length=60, verbose_name='Prénoms')),
                ('gender', models.CharField(choices=[('H', 'Homme'), ('F', 'Femme'), ('O', 'Autre')], default='H', max_length=1, verbose_name='Genre')),
                ('birthday', models.DateField(verbose_name='Date de naissance')),
                ('phone_number', models.CharField(max_length=15, verbose_name='Téléphone')),
                ('url_picture', models.CharField(max_length=255, verbose_name="Lien de l'image")),
                ('active', models.BooleanField(default=False, verbose_name='Actif')),
                ('matricule', models.CharField(max_length=50, verbose_name='Matricule')),
                ('phone_number_father', models.CharField(max_length=15, verbose_name='Téléphone du père')),
            ],
            options={
                'verbose_name': 'Eleve',
                'verbose_name_plural': 'Eleves',
            },
        ),
        migrations.CreateModel(
            name='TeacherModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
                ('first_name', models.CharField(max_length=30, verbose_name='Nom')),
                ('last_name', models.CharField(max_length=60, verbose_name='Prénoms')),
                ('gender', models.CharField(choices=[('H', 'Homme'), ('F', 'Femme'), ('O', 'Autre')], default='H', max_length=1, verbose_name='Genre')),
                ('birthday', models.DateField(verbose_name='Date de naissance')),
                ('phone_number', models.CharField(max_length=15, verbose_name='Téléphone')),
                ('url_picture', models.CharField(max_length=255, verbose_name="Lien de l'image")),
                ('active', models.BooleanField(default=False, verbose_name='Actif')),
                ('available', models.CharField(default=True, verbose_name='Disponible')),
                ('speciality', models.CharField(max_length=50, verbose_name='Spécialité')),
            ],
            options={
                'verbose_name': 'Professeur',
                'verbose_name_plural': 'Professeurs',
            },
        ),
    ]
