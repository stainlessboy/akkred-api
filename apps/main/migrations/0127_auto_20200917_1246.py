# Generated by Django 2.1.2 on 2020-09-17 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0126_auto_20200904_1628'),
    ]

    operations = [
        migrations.AlterField(
            model_name='confirmreestr',
            name='reissue_date',
            field=models.DateField(blank=True, null=True, verbose_name='Qayta rasmiylashtirilgan sana'),
        ),
    ]
