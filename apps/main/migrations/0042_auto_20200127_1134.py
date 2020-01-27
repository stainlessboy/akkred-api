# Generated by Django 2.1.2 on 2020-01-27 11:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0041_documentform'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documentform',
            name='document',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='document_forms', to='main.Document'),
        ),
    ]