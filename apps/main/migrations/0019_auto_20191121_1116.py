# Generated by Django 2.1.2 on 2019-11-21 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_document_number'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registries',
            old_name='title_applicant',
            new_name='title_yurd_lisa',
        ),
        migrations.AlterField(
            model_name='registries',
            name='form_ownership',
            field=models.CharField(editable=False, max_length=455, null=True),
        ),
        migrations.AlterField(
            model_name='registries',
            name='full_name_supervisor_main',
            field=models.CharField(editable=False, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='registries',
            name='position_supervisor_ao',
            field=models.CharField(editable=False, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='registries',
            name='position_supervisor_legal',
            field=models.CharField(editable=False, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='registries',
            name='web_site_ao',
            field=models.CharField(editable=False, max_length=255, null=True),
        ),
    ]
