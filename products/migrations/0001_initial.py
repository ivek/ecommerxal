# Generated by Django 2.2.7 on 2019-12-23 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='products/')),
                ('slug', models.SlugField(unique=True)),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=8)),
                ('create_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
