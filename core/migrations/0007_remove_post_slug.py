# Generated by Django 4.0.4 on 2022-05-12 15:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_post_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='slug',
        ),
    ]