# Generated by Django 2.1.2 on 2019-10-04 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20190912_1518'),
    ]

    operations = [
        migrations.AddField(
            model_name='staticpage',
            name='type',
            field=models.CharField(choices=[('about', 'about'), ('action', 'action'), ('documentation', 'documentation'), ('information', 'information'), ('apply', 'apply'), ('contact', 'contact')], default='about', max_length=255),
        ),
    ]
