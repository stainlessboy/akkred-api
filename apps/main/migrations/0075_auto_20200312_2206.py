# Generated by Django 2.1.2 on 2020-03-12 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0074_registries_itt_cd'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registries',
            name='itt_cd',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
