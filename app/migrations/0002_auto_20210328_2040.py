# Generated by Django 3.1.7 on 2021-03-28 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carros',
            name='entrada',
            field=models.CharField(max_length=100),
        ),
    ]