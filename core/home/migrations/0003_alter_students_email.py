# Generated by Django 5.0.4 on 2024-05-04 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_students_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]
