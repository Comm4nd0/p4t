# Generated by Django 2.1.1 on 2018-09-15 20:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0009_auto_20180915_2049'),
    ]

    operations = [
        migrations.RenameField(
            model_name='overview',
            old_name='image',
            new_name='image_800x800',
        ),
    ]
