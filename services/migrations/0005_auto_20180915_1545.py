# Generated by Django 2.1.1 on 2018-09-15 15:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0004_auto_20180915_1531'),
    ]

    operations = [
        migrations.RenameField(
            model_name='main',
            old_name='title',
            new_name='sub_heading',
        ),
    ]
