# Generated by Django 2.1.1 on 2018-09-16 09:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('paws4thought', '0012_auto_20180916_0845'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CompanyPage',
            new_name='CompanyDetail',
        ),
        migrations.RenameModel(
            old_name='TeamPage',
            new_name='TeamDetail',
        ),
    ]