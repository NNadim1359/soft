# Generated by Django 2.2.6 on 2019-11-17 05:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flex', '0005_flexpage_flex_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='flexpage',
            old_name='flex_image',
            new_name='page_banner_image',
        ),
    ]
