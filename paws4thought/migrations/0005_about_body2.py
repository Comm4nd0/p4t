# Generated by Django 2.1.1 on 2018-09-15 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paws4thought', '0004_auto_20180915_2337'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='body2',
            field=models.TextField(blank=True),
        ),
    ]
