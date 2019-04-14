# Generated by Django 2.1.7 on 2019-04-13 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0006_auto_20190413_1802'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentNotifications',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_id', models.CharField(max_length=50, null=True)),
                ('kyc', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=20)),
                ('metadata', models.CharField(max_length=500)),
            ],
        ),
    ]