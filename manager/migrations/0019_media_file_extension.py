# Generated by Django 3.1.7 on 2021-03-28 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0018_remove_media_file_extension'),
    ]

    operations = [
        migrations.AddField(
            model_name='media',
            name='file_extension',
            field=models.CharField(blank=True, editable=False, max_length=16, null=True),
        ),
    ]
