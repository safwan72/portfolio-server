# Generated by Django 3.2.6 on 2022-01-16 21:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App_Main', '0002_auto_20211004_0024'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ResumeDetailsEducation',
        ),
        migrations.DeleteModel(
            name='ResumeExperienceDetails',
        ),
    ]