# Generated by Django 2.1.1 on 2018-09-15 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0010_auto_20180915_2051'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='main_image_500x400',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]