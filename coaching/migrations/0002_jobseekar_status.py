# Generated by Django 4.1.2 on 2022-12-18 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coaching', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobseekar',
            name='status',
            field=models.CharField(default='', max_length=50),
        ),
    ]