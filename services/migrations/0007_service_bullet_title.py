# Generated by Django 2.1.1 on 2018-09-15 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0006_auto_20180915_1551'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='bullet_title',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
