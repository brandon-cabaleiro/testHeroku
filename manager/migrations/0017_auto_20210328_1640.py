# Generated by Django 3.1.7 on 2021-03-28 16:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0016_auto_20210328_1625'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recordingsession',
            name='location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='manager.physicallocation'),
        ),
    ]
