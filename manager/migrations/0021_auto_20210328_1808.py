# Generated by Django 3.1.7 on 2021-03-28 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0020_auto_20210328_1738'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='media',
            field=models.ManyToManyField(blank=True, related_name='personnel', to='manager.Media'),
        ),
    ]
