# Generated by Django 5.1 on 2024-09-01 02:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0003_remove_studentmodel_adress_id_and_more'),
        ('user', '0002_alter_usermodel_school_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='adressmodel',
            name='student_id',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='adress_student_ids', to='school.studentmodel'),
        ),
        migrations.AddField(
            model_name='adressmodel',
            name='teacher_id',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='adress_teacher_ids', to='school.teachermodel'),
        ),
        migrations.AddField(
            model_name='usermodel',
            name='student_id',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_student_ids', to='school.studentmodel'),
        ),
        migrations.AddField(
            model_name='usermodel',
            name='teacher_id',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_teacher_ids', to='school.teachermodel'),
        ),
        migrations.AlterField(
            model_name='adressmodel',
            name='city',
            field=models.CharField(max_length=50, verbose_name='Ville '),
        ),
        migrations.AlterField(
            model_name='adressmodel',
            name='country',
            field=models.CharField(max_length=50, verbose_name='Pays '),
        ),
        migrations.AlterField(
            model_name='adressmodel',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Date de création '),
        ),
        migrations.AlterField(
            model_name='adressmodel',
            name='status',
            field=models.BooleanField(default=True, verbose_name='Status '),
        ),
        migrations.AlterField(
            model_name='adressmodel',
            name='street',
            field=models.CharField(max_length=50, verbose_name='Quartier '),
        ),
        migrations.AlterField(
            model_name='adressmodel',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name="Date d'édition "),
        ),
        migrations.AlterField(
            model_name='roleusermodel',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Date de création '),
        ),
        migrations.AlterField(
            model_name='roleusermodel',
            name='role',
            field=models.CharField(max_length=255, verbose_name="Rôle de l'utilisateur "),
        ),
        migrations.AlterField(
            model_name='roleusermodel',
            name='status',
            field=models.BooleanField(default=True, verbose_name='Status '),
        ),
        migrations.AlterField(
            model_name='roleusermodel',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name="Date d'édition "),
        ),
    ]