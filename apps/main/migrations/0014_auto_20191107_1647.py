# Generated by Django 2.1.2 on 2019-11-07 16:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_auto_20191107_1647'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registries',
            old_name='full_name_supervisor',
            new_name='full_name_supervisor_ao',
        ),
    ]
