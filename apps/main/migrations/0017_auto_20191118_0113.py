# Generated by Django 2.1.2 on 2019-11-18 01:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_auto_20191118_0106'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='email',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='phone',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
