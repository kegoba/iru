# Generated by Django 2.2.3 on 2020-01-06 18:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200101_1805'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comments',
            old_name='post',
            new_name='post_comment',
        ),
    ]
