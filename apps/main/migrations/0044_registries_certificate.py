# Generated by Django 2.1.2 on 2020-01-30 09:58

from django.db import migrations, models
import main.models.registries


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0043_auto_20200128_2237'),
    ]

    operations = [
        migrations.AddField(
            model_name='registries',
            name='certificate',
            field=models.FileField(blank=True, null=True, upload_to=main.models.registries.upload_name),
        ),
    ]
