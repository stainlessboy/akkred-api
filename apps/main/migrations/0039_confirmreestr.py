# Generated by Django 2.1.2 on 2020-01-10 16:42

from django.db import migrations, models
import django.db.models.deletion
import main.models.confirm_reestr


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0038_employee_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConfirmReestr',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('number', models.CharField(max_length=255, null=True)),
                ('inn', models.CharField(max_length=455, null=True)),
                ('title_yurd_lisa', models.CharField(max_length=1000, null=True)),
                ('phone', models.CharField(max_length=255, null=True)),
                ('email', models.CharField(max_length=255, null=True)),
                ('web_site', models.CharField(blank=True, max_length=255, null=True)),
                ('title_organ', models.CharField(max_length=255)),
                ('address_organ', models.CharField(max_length=1000, null=True)),
                ('accreditation_date', models.DateField(null=True)),
                ('full_name_supervisor_ao', models.CharField(max_length=255, null=True)),
                ('status', models.CharField(choices=[('active', 'active'), ('inactive', 'inactive'), ('paused', 'paused'), ('extended', 'extended')], default='inactive', max_length=20)),
                ('podpisal', models.CharField(max_length=400)),
                ('text', models.TextField(blank=True, null=True)),
                ('file_oblast', models.FileField(blank=True, null=True, upload_to=main.models.confirm_reestr.upload_name)),
                ('region', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='confirm_reestrs', to='main.Region')),
                ('type_organ', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='confirm_reestrs', to='main.TypeOrgan')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
