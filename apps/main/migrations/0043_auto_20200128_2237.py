# Generated by Django 2.1.2 on 2020-01-28 22:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0042_auto_20200127_1134'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categoryreestrinfouser',
            options={'verbose_name': 'Категория П.П.В', 'verbose_name_plural': 'Категория П.П.В'},
        ),
        migrations.AlterModelOptions(
            name='confirmreestr',
            options={'verbose_name': 'Реестр одобренных лабораторий', 'verbose_name_plural': 'Реестр одобренных лабораторий'},
        ),
        migrations.AlterModelOptions(
            name='docparent',
            options={'verbose_name': 'Категория Документа', 'verbose_name_plural': 'Категории Документов'},
        ),
        migrations.AlterModelOptions(
            name='doctype',
            options={'verbose_name': 'Тип Документа', 'verbose_name_plural': 'Типы Документов'},
        ),
        migrations.AlterModelOptions(
            name='document',
            options={'verbose_name': 'Документ', 'verbose_name_plural': 'Документы'},
        ),
        migrations.AlterModelOptions(
            name='documentform',
            options={'verbose_name': 'Форма Документа ', 'verbose_name_plural': 'Форма Документа'},
        ),
        migrations.AlterModelOptions(
            name='employee',
            options={'verbose_name': 'Сотрудник', 'verbose_name_plural': 'Сотрудники'},
        ),
        migrations.AlterModelOptions(
            name='inspectioncontrol',
            options={'ordering': ['-id'], 'verbose_name': 'Инспекционный контроль', 'verbose_name_plural': 'Инспекционные контроли'},
        ),
        migrations.AlterModelOptions(
            name='mediafile',
            options={'verbose_name': 'Библиотека файлов', 'verbose_name_plural': 'Библиотека фалов'},
        ),
        migrations.AlterModelOptions(
            name='news',
            options={'ordering': ['-id'], 'verbose_name': 'Новость', 'verbose_name_plural': 'Новости'},
        ),
        migrations.AlterModelOptions(
            name='question',
            options={'verbose_name': 'Вопрос-ответ', 'verbose_name_plural': 'Вопрос-ответы'},
        ),
        migrations.AlterModelOptions(
            name='reestrinfouser',
            options={'verbose_name': 'Информация о приостановленных, прекрашенных и возобновленных свидетельствах об аккредитации', 'verbose_name_plural': 'Информация о приостановленных, прекрашенных и возобновленных свидетельствах об аккредитации'},
        ),
        migrations.AlterModelOptions(
            name='region',
            options={'ordering': ['-id'], 'verbose_name': 'Регион', 'verbose_name_plural': 'Регионы'},
        ),
        migrations.AlterModelOptions(
            name='registries',
            options={'verbose_name': 'Государственный реестр аккредитованных ООС и МС', 'verbose_name_plural': 'Государственный реестр аккредитованных ООС и МС'},
        ),
        migrations.AlterModelOptions(
            name='satisfactionquestionnaire',
            options={'ordering': ['-id'], 'verbose_name': 'Оценка удовлетворенности потребителей', 'verbose_name_plural': 'Оценка удовлетворенности потребителей'},
        ),
        migrations.AlterModelOptions(
            name='slider',
            options={'verbose_name': 'Слайдер', 'verbose_name_plural': 'Слайдеры'},
        ),
        migrations.AlterModelOptions(
            name='staticpage',
            options={'ordering': ['-id'], 'verbose_name': 'Страница', 'verbose_name_plural': 'Страницы'},
        ),
        migrations.AlterModelOptions(
            name='typeorgan',
            options={'verbose_name': 'Орган', 'verbose_name_plural': 'Орган'},
        ),
    ]