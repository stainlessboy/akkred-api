# Generated by Django 2.1.2 on 2020-02-13 11:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0059_auto_20200213_1149'),
    ]

    operations = [
        migrations.CreateModel(
            name='CaseType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
            ],
        ),
        migrations.AddField(
            model_name='registerstatuslog',
            name='case_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reestr_logs', to='main.CaseType'),
        ),
    ]
