# Generated by Django 3.0.8 on 2020-08-24 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lectures', '0009_auto_20200723_1706'),
    ]

    operations = [
        migrations.AddField(
            model_name='lecture',
            name='image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
