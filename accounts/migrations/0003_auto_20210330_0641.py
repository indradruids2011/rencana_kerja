# Generated by Django 3.1.7 on 2021-03-30 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20210330_0635'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='useraccount',
            name='user_id',
        ),
        migrations.AddField(
            model_name='useraccount',
            name='username',
            field=models.CharField(default=1, max_length=20, unique=True),
            preserve_default=False,
        ),
    ]
