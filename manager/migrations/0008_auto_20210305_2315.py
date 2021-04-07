# Generated by Django 3.1.7 on 2021-03-05 23:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0007_auto_20210305_2311'),
    ]

    operations = [
        migrations.CreateModel(
            name='RecordingSession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=500)),
                ('date', models.DateTimeField()),
            ],
        ),
        migrations.AlterField(
            model_name='artist',
            name='media',
            field=models.ManyToManyField(blank=True, to='manager.Media'),
        ),
        migrations.AlterField(
            model_name='artist',
            name='tags',
            field=models.ManyToManyField(blank=True, to='manager.Tag'),
        ),
        migrations.AlterField(
            model_name='media',
            name='date_published',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='media',
            name='description',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='media',
            name='digital_location',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='media',
            name='is_physical',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='media',
            name='physical_location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='manager.physicallocation'),
        ),
        migrations.AlterField(
            model_name='media',
            name='tags',
            field=models.ManyToManyField(blank=True, to='manager.Tag'),
        ),
        migrations.DeleteModel(
            name='Session',
        ),
        migrations.AddField(
            model_name='recordingsession',
            name='artists',
            field=models.ManyToManyField(blank=True, to='manager.Artist'),
        ),
        migrations.AddField(
            model_name='recordingsession',
            name='media',
            field=models.ManyToManyField(blank=True, to='manager.Media'),
        ),
    ]