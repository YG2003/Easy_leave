# Generated by Django 4.1.3 on 2022-11-28 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_record'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='end_date',
            field=models.DateField(null=True, verbose_name='End date of leave'),
        ),
        migrations.AddField(
            model_name='application',
            name='start_date',
            field=models.DateField(null=True, verbose_name='Start date of leave'),
        ),
    ]
