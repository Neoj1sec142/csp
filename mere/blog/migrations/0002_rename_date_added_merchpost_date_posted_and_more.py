# Generated by Django 4.0.6 on 2022-07-15 00:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='merchpost',
            old_name='date_added',
            new_name='date_posted',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='date_added',
            new_name='date_posted',
        ),
    ]
