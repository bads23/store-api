# Generated by Django 2.1.7 on 2019-08-05 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0004_auto_20190730_2214'),
    ]

    operations = [
        migrations.AddField(
            model_name='clients',
            name='tag',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]