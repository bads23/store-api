# Generated by Django 2.1.7 on 2019-03-27 09:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20190324_1827'),
    ]

    operations = [
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.URLField()),
                ('is_avatar', models.BooleanField(null=True)),
                ('catalog', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='images', to='products.Catalog')),
            ],
        ),
        migrations.AlterField(
            model_name='inventory',
            name='product',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='stock', to='products.Catalog'),
        ),
    ]
