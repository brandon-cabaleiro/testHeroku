# Generated by Django 3.1.7 on 2021-03-11 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0010_recordingsession_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='media',
            options={'verbose_name_plural': 'media'},
        ),
        migrations.AlterField(
            model_name='media',
            name='description',
            field=models.TextField(blank=True, max_length=2000, null=True),
        ),
    ]
