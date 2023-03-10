# Generated by Django 4.1.2 on 2023-01-11 03:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coaching', '0035_alter_education_jobseekerprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobseekerprofile',
            name='graduation_percentage',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='jobseekerprofile',
            name='graduation_stream',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='jobseekerprofile',
            name='graduation_year',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='jobseekerprofile',
            name='post_graduation_percentage',
            field=models.CharField(blank=True, default=None, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='jobseekerprofile',
            name='post_graduation_stream',
            field=models.CharField(blank=True, default=None, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='jobseekerprofile',
            name='post_graduation_year',
            field=models.CharField(blank=True, default=None, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='jobseekerprofile',
            name='primary_percentage',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='jobseekerprofile',
            name='primary_stream',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='jobseekerprofile',
            name='primary_year',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='jobseekerprofile',
            name='secondary_percentage',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='jobseekerprofile',
            name='secondary_stream',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='jobseekerprofile',
            name='secondary_year',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='posted_date',
            field=models.DateField(default=datetime.date(2023, 1, 11)),
        ),
        migrations.AlterField(
            model_name='jobseekerprofile',
            name='resume',
            field=models.FileField(default='', upload_to=''),
        ),
        migrations.DeleteModel(
            name='Education',
        ),
    ]
