# Generated by Django 2.1.2 on 2020-08-12 16:04

from django.db import migrations, models
import main.models.confirm_reestr


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0115_auto_20200810_1133'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='confirmreestr',
            name='type_organ',
        ),
        migrations.AddField(
            model_name='confirmreestr',
            name='certificate',
            field=models.FileField(blank=True, null=True, upload_to=main.models.confirm_reestr.upload_name),
        ),
        migrations.AddField(
            model_name='confirmreestr',
            name='qr_code',
            field=models.ImageField(blank=True, null=True, upload_to=main.models.confirm_reestr.upload_name),
        ),
    ]