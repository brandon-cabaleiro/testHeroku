# Generated by Django 3.1.7 on 2021-03-11 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0011_auto_20210311_2031'),
    ]

    operations = [
        migrations.AddField(
            model_name='media',
            name='file_extension',
            field=models.CharField(blank=True, max_length=16, null=True),
        ),
    ]
