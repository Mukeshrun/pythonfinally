# Generated by Django 4.1.2 on 2022-12-20 03:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coaching', '0006_remove_jobseekerprofile_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobseekar',
            name='user',
        ),
    ]
