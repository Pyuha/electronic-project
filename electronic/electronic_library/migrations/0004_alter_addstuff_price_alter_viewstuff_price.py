# Generated by Django 4.2.1 on 2023-06-04 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('electronic_library', '0003_addstuff'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addstuff',
            name='price',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='viewstuff',
            name='price',
            field=models.IntegerField(),
        ),
    ]
