# Generated by Django 2.1 on 2018-10-29 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitio', '0003_auto_20181028_2040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perro',
            name='fotografia',
            field=models.ImageField(upload_to='media'),
        ),
    ]