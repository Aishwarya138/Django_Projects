# Generated by Django 3.2.15 on 2022-09-17 09:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20220917_1419'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Content',
            new_name='Post',
        ),
    ]
