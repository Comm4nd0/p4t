# Generated by Django 2.1.1 on 2018-09-15 15:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0004_auto_20180915_1531'),
        ('gallery', '0003_auto_20180915_1542'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Gallery',
            new_name='Image',
        ),
    ]
