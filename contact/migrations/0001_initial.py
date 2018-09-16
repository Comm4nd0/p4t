# Generated by Django 2.1.1 on 2018-09-16 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page_title', models.CharField(blank=True, max_length=100)),
                ('header_image_1600x660', models.ImageField(blank=True, upload_to='')),
                ('sub_heading', models.CharField(blank=True, max_length=100)),
                ('email', models.CharField(blank=True, max_length=100)),
                ('landline', models.CharField(blank=True, max_length=100)),
                ('mobile', models.CharField(blank=True, max_length=100)),
                ('address', models.CharField(blank=True, max_length=200)),
                ('body', models.TextField(blank=True)),
                ('image_600x350', models.ImageField(blank=True, upload_to='')),
                ('form_heading', models.CharField(blank=True, max_length=100)),
                ('send_button_text', models.CharField(blank=True, max_length=100)),
            ],
        ),
    ]