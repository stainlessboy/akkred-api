# Generated by Django 2.1.2 on 2020-07-07 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0107_auto_20200706_1720'),
    ]

    operations = [
        migrations.AddField(
            model_name='registries',
            name='is_public',
            field=models.BooleanField(default=True),
        ),
    ]
