# Generated by Django 4.1 on 2022-11-08 05:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_application_status'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Manager',
        ),
        migrations.RemoveField(
            model_name='worker',
            name='email',
        ),
        migrations.RemoveField(
            model_name='worker',
            name='password',
        ),
        migrations.RemoveField(
            model_name='worker',
            name='phone',
        ),
    ]
