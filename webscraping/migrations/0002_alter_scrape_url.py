# Generated by Django 4.1.1 on 2022-09-18 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webscraping', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scrape',
            name='url',
            field=models.CharField(max_length=200),
        ),
    ]
