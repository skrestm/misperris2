# Generated by Django 2.1 on 2018-11-02 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitio', '0007_adopcion'),
    ]

    operations = [
        migrations.AddField(
            model_name='perro',
            name='adoptador_por',
            field=models.TextField(null=True, verbose_name='Adoptado por'),
        ),
    ]
