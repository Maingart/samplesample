# Generated by Django 3.2 on 2021-04-23 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweet', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='tweet',
            name='photo',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]