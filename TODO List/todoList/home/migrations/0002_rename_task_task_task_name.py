# Generated by Django 3.2.5 on 2021-09-23 06:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='task',
            new_name='task_name',
        ),
    ]
