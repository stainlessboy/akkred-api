# Generated by Django 2.1.2 on 2020-05-07 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0085_auto_20200507_0000'),
    ]

    operations = [
        migrations.AddField(
            model_name='registries',
            name='oked',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='registries',
            name='okonx',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
