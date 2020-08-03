# Generated by Django 2.1.2 on 2020-08-03 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0112_auto_20200803_2152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='confirmreestr',
            name='accreditation_date',
            field=models.DateField(null=True, verbose_name="Reestrda ro'yxatga olingan sana"),
        ),
        migrations.AlterField(
            model_name='confirmreestr',
            name='address',
            field=models.CharField(max_length=255, null=True, verbose_name='Joylashgan manzil'),
        ),
        migrations.AlterField(
            model_name='confirmreestr',
            name='address_organ',
            field=models.CharField(max_length=1000, null=True, verbose_name='Yuridik manzil'),
        ),
        migrations.AlterField(
            model_name='confirmreestr',
            name='number',
            field=models.CharField(max_length=255, null=True, verbose_name="Reestrda ro'yxat raqami"),
        ),
        migrations.AlterField(
            model_name='confirmreestr',
            name='reissue_date',
            field=models.DateField(null=True, verbose_name='Qayta rasmiylashtirilgan sana'),
        ),
        migrations.AlterField(
            model_name='confirmreestr',
            name='validity_date',
            field=models.DateField(null=True, verbose_name='Amal qilish muddati'),
        ),
    ]
