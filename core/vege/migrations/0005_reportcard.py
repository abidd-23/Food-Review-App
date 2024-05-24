# Generated by Django 5.0.4 on 2024-05-23 09:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vege', '0004_subject_subjectmarks'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReportCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_reportCard_generation', models.DateField(auto_created=True)),
                ('student_rank', models.IntegerField()),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='studentreportcard', to='vege.student')),
            ],
        ),
    ]
