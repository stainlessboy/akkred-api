# Generated by Django 2.1.2 on 2020-08-19 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0119_auto_20200814_1355'),
    ]

    operations = [
        migrations.AddField(
            model_name='confirmreestr',
            name='title_organ_short',
            field=models.CharField(max_length=255, null=True, verbose_name='Sokrashenniy title yur lisa'),
        ),
    ]
