# Generated by Django 4.1.7 on 2023-07-12 05:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0008_delete_studentrecord'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historicalstudent',
            name='school_id_number',
        ),
        migrations.RemoveField(
            model_name='student',
            name='school_id_number',
        ),
    ]
