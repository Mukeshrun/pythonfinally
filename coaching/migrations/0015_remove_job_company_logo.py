# Generated by Django 4.1.2 on 2022-12-23 02:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coaching', '0014_job_company_logo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='company_logo',
        ),
    ]
