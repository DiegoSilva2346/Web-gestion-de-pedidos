# Generated by Django 3.1 on 2020-09-17 19:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_post_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='slug',
        ),
    ]
