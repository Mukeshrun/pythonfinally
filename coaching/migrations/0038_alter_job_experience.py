# Generated by Django 4.1.2 on 2023-01-19 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coaching', '0037_alter_job_posted_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='experience',
            field=models.CharField(max_length=25, null=True),
        ),
    ]