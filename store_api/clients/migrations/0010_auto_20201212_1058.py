# Generated by Django 2.2.10 on 2020-12-12 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0009_music'),
    ]

    operations = [
        migrations.AddField(
            model_name='music',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='music',
            name='plays',
            field=models.IntegerField(default=0),
        ),
    ]
