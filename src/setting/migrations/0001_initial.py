# Generated by Django 5.1 on 2024-08-31 10:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('school', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppSettingModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
                ('smtp_server', models.CharField(max_length=50, verbose_name='Server SMTP')),
                ('smtp_port', models.IntegerField(verbose_name='Port SMTP')),
                ('smtp_username', models.CharField(max_length=50, verbose_name="Nom d'utilisateur SMTP")),
                ('smtp_password', models.CharField(max_length=128, verbose_name='Mot de passe SMTP')),
                ('school_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='app_setting_school_ids', to='school.schoolmodel')),
            ],
            options={
                'verbose_name': 'Paramètre appli',
                'verbose_name_plural': 'Paramètre appli',
            },
        ),
    ]