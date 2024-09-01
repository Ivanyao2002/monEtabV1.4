# Generated by Django 5.1 on 2024-08-31 10:52

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('school', '0001_initial'),
        ('user', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='studentmodel',
            name='adress_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='student_adress_ids', to='user.adressmodel'),
        ),
        migrations.AddField(
            model_name='studentmodel',
            name='user_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='student_user_ids', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='studentcardsmodel',
            name='student_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_cards_student_ids', to='school.studentmodel'),
        ),
        migrations.AddField(
            model_name='absencemodel',
            name='student_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='absence_student_ids', to='school.studentmodel'),
        ),
        migrations.AddField(
            model_name='teachermodel',
            name='adress_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='teacher_adress_ids', to='user.adressmodel'),
        ),
        migrations.AddField(
            model_name='teachermodel',
            name='user_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='teacher_user_ids', to=settings.AUTH_USER_MODEL),
        ),
    ]