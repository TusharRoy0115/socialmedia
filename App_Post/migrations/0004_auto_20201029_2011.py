# Generated by Django 3.1.2 on 2020-10-29 14:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App_Post', '0003_post_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='slug',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]