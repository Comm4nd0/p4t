# Generated by Django 2.1.1 on 2018-09-16 12:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_contactdetail_image_500x600_homepage'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contactdetail',
            old_name='image_500x600_homepage',
            new_name='image_700x458_homepage',
        ),
    ]
