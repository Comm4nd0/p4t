# Generated by Django 2.1.1 on 2018-09-16 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paws4thought', '0007_company_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='home_page_image_800x1000',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
