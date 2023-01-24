# Generated by Django 4.1.2 on 2022-12-19 03:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('coaching', '0002_jobseekar_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Jobseekerprofile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photopath', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('mobile', models.IntegerField(default='')),
                ('dob', models.DateField()),
                ('education', models.CharField(max_length=400)),
                ('resume', models.CharField(max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coaching.jobseekar')),
            ],
        ),
        migrations.DeleteModel(
            name='Userdetail',
        ),
    ]
