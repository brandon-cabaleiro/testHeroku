# Generated by Django 3.1.7 on 2021-03-28 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0013_auto_20210328_1534'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='person',
            options={'verbose_name_plural': 'personnel'},
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]