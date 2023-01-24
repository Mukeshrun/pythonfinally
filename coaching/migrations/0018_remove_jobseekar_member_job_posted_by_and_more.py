# Generated by Django 4.1.2 on 2022-12-23 05:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('coaching', '0017_alter_job_logo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobseekar',
            name='member',
        ),
        migrations.AddField(
            model_name='job',
            name='posted_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='jobseekar',
            name='branch',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='jobseekar',
            name='course',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='job',
            name='logo',
            field=models.ImageField(default='/media/download.png', upload_to=''),
        ),
    ]