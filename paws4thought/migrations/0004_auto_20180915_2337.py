# Generated by Django 2.1.1 on 2018-09-15 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paws4thought', '0003_auto_20180915_2336'),
    ]

    operations = [
        migrations.AddField(
            model_name='feature',
            name='body',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='feature',
            name='title',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
