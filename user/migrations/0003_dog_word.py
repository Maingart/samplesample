# Generated by Django 3.2 on 2021-04-22 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20210422_0241'),
    ]

    operations = [
        migrations.AddField(
            model_name='dog',
            name='word',
            field=models.CharField(default='gav', max_length=12),
        ),
    ]