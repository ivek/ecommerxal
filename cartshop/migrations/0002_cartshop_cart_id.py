# Generated by Django 2.2.7 on 2019-12-23 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cartshop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartshop',
            name='cart_id',
            field=models.CharField(default='', max_length=100, unique=True),
            preserve_default=False,
        ),
    ]
