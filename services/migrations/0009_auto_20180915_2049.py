# Generated by Django 2.1.1 on 2018-09-15 20:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0008_service_intro_bold_text'),
    ]

    operations = [
        migrations.RenameField(
            model_name='service',
            old_name='header_image',
            new_name='header_image_1600x660',
        ),
    ]
