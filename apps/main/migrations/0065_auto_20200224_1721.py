# Generated by Django 2.1.2 on 2020-02-24 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0064_auto_20200222_0014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registriesstatus',
            name='status',
            field=models.CharField(choices=[('active', 'Возобновлено'), ('inactive', 'Прекращено'), ('paused', 'Приостановлено'), ('done', 'Подтверждено'), ('renewed', 'Переоформлено')], default='inactive', max_length=20),
        ),
    ]
