# Generated by Django 2.1.2 on 2020-03-31 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0079_auto_20200331_1314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registries',
            name='status',
            field=models.CharField(choices=[('active', 'Действующий'), ('inactive', 'Прекращен'), ('paused', 'Приостановлен'), ('extended', 'Продлен'), ('temporarily_resumed', 'Временно возобновлен')], default='inactive', max_length=20),
        ),
    ]
