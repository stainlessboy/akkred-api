# Generated by Django 2.1.2 on 2019-11-07 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20191107_1307'),
    ]

    operations = [
        migrations.AddField(
            model_name='registries',
            name='address_applicant',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='registries',
            name='position_supervisor_legal',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='registries',
            name='title_applicant',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
