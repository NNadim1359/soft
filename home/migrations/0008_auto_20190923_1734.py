# Generated by Django 2.2.5 on 2019-09-23 11:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20190923_1618'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homepage',
            name='banner_image',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='banner_subtitle',
        ),
    ]
