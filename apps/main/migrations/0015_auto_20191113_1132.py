# Generated by Django 2.1.2 on 2019-11-13 11:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_auto_20191107_1647'),
    ]

    operations = [
        migrations.CreateModel(
            name='Laws',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('name_ru', models.TextField(null=True)),
                ('name_en', models.TextField(null=True)),
                ('name_uz', models.TextField(null=True)),
                ('name2', models.TextField()),
                ('name2_ru', models.TextField(null=True)),
                ('name2_en', models.TextField(null=True)),
                ('name2_uz', models.TextField(null=True)),
                ('link', models.CharField(max_length=300)),
                ('link_ru', models.CharField(max_length=300, null=True)),
                ('link_en', models.CharField(max_length=300, null=True)),
                ('link_uz', models.CharField(max_length=300, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='LawsCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
            ],
        ),
        migrations.AddField(
            model_name='laws',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='laws', to='main.LawsCategory'),
        ),
    ]
