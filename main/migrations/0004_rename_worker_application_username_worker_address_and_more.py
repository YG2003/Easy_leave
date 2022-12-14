# Generated by Django 4.1 on 2022-11-24 09:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0003_delete_manager_remove_worker_email_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='application',
            old_name='worker',
            new_name='username',
        ),
        migrations.AddField(
            model_name='worker',
            name='address',
            field=models.TextField(default='Pending', verbose_name='Address'),
        ),
        migrations.AddField(
            model_name='worker',
            name='email',
            field=models.EmailField(default='Pending', max_length=254, verbose_name='Email'),
        ),
        migrations.AddField(
            model_name='worker',
            name='first_name',
            field=models.CharField(default='Pending', max_length=50, verbose_name='First Name'),
        ),
        migrations.AddField(
            model_name='worker',
            name='last_name',
            field=models.CharField(default='Pending', max_length=50, verbose_name='Last Name'),
        ),
        migrations.AddField(
            model_name='worker',
            name='phone',
            field=models.CharField(default='Pending', max_length=10, verbose_name='Mobile number'),
        ),
        migrations.AlterField(
            model_name='worker',
            name='username',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
