# Generated by Django 2.1.2 on 2020-01-07 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0037_satisfactionquestionnaire'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='order',
            field=models.PositiveIntegerField(default=0),
        ),
    ]