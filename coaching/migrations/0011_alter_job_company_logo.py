# Generated by Django 4.1.2 on 2022-12-21 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coaching', '0010_job_company_address_job_company_logo_job_end_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='company_logo',
            field=models.ImageField(default='/media/download.png', upload_to=''),
        ),
    ]