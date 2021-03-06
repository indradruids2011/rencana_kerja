# Generated by Django 3.1.7 on 2021-03-30 07:04

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20210330_0641'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bidang',
            name='bidang_id',
        ),
        migrations.RemoveField(
            model_name='role',
            name='role_id',
        ),
        migrations.AddField(
            model_name='bidang',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bidang',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='role',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='role',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
