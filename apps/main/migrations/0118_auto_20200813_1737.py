# Generated by Django 2.1.2 on 2020-08-13 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0117_confirmreestr_area'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='confirmreestr',
            name='accreditation_duration',
        ),
        migrations.AddField(
            model_name='confirmreestr',
            name='title_organ_type',
            field=models.CharField(max_length=255, null=True, verbose_name='Yuridik shaxs mulkchilik shakli'),
        ),
        migrations.AlterField(
            model_name='confirmreestr',
            name='title_organ',
            field=models.CharField(max_length=255, verbose_name='Yuridik shaxs nomi'),
        ),
        migrations.AlterField(
            model_name='confirmreestr',
            name='title_yurd_lisa',
            field=models.CharField(max_length=1000, null=True, verbose_name='sinov laboratoriyasi nomi'),
        ),
    ]
