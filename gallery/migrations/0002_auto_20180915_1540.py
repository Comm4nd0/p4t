# Generated by Django 2.1.1 on 2018-09-15 15:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0004_auto_20180915_1531'),
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Image',
            new_name='Gallery',
        ),
    ]
