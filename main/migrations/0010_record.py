# Generated by Django 4.1.3 on 2022-11-28 11:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0009_admin'),
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.IntegerField(default=0, verbose_name='Total applications sent')),
                ('accepted', models.IntegerField(default=0, verbose_name='Accepted applications')),
                ('rejected', models.IntegerField(default=0, verbose_name='Rejected Applications')),
                ('last_date', models.DateField(null=True, verbose_name='Last application sent on')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
