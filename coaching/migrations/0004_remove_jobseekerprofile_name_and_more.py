# Generated by Django 4.1.2 on 2022-12-19 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coaching', '0003_jobseekerprofile_delete_userdetail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobseekerprofile',
            name='name',
        ),
        migrations.AddField(
            model_name='jobseekerprofile',
            name='username',
            field=models.CharField(default='', max_length=100),
        ),
    ]
