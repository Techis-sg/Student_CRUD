# Generated by Django 3.2.7 on 2021-09-04 19:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='DOB',
            new_name='dob',
        ),
    ]