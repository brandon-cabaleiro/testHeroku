# Generated by Django 3.1.7 on 2021-03-11 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0009_auto_20210305_2316'),
    ]

    operations = [
        migrations.AddField(
            model_name='recordingsession',
            name='name',
            field=models.CharField(default='', max_length=500),
            preserve_default=False,
        ),
    ]