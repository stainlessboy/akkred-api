# Generated by Django 2.1.2 on 2020-05-25 11:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0090_auto_20200519_1731'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='number',
        ),
        migrations.RemoveField(
            model_name='document',
            name='title',
        ),
    ]
