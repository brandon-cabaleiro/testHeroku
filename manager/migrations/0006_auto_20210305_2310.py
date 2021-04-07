# Generated by Django 3.1.7 on 2021-03-05 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0005_session'),
    ]

    operations = [
        migrations.AddField(
            model_name='session',
            name='location',
            field=models.CharField(default='', max_length=500),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='artist',
            name='duration_active',
            field=models.DurationField(null=True),
        ),
        migrations.AlterField(
            model_name='artist',
            name='tags',
            field=models.ManyToManyField(null=True, to='manager.Tag'),
        ),
    ]