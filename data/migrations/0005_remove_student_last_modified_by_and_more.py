# Generated by Django 4.1.7 on 2023-06-23 00:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0004_student_last_modified_by_student_last_modified_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='last_modified_by',
        ),
        migrations.RemoveField(
            model_name='student',
            name='last_modified_date',
        ),
        migrations.RemoveField(
            model_name='studentrecord',
            name='last_modified_by',
        ),
        migrations.RemoveField(
            model_name='studentrecord',
            name='last_modified_date',
        ),
        migrations.RemoveField(
            model_name='studentrecord',
            name='last_updated',
        ),
        migrations.RemoveField(
            model_name='studentrecord',
            name='timestamp',
        ),
    ]
