# Generated by Django 4.1.2 on 2022-12-28 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coaching', '0021_job_programming_language'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='job_detail',
            field=models.TextField(max_length=500),
        ),
    ]
