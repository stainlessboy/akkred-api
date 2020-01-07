# Generated by Django 2.1.2 on 2019-12-26 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0036_auto_20191214_0138'),
    ]

    operations = [
        migrations.CreateModel(
            name='SatisfactionQuestionnaire',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_of_activity', models.CharField(choices=[('testing_laboratory', 'испытательная лаборатория'), ('calibration_laboratory', 'калибровочная лаборатория'), ('pov_calibration_laboratory', 'поверочная лаборатория'), ('medical_laboratory', 'медицинская лаборатория'), ('product_certification_body', 'орган по сертификации продукции'), ('authority_for_certification_of_services', 'орган по сертификации услуг'), ('management_system_certification_body', 'орган по сертификации систем менеджмента'), ('personnel_certification_body', 'орган по сертификации персонала'), ('inspection_body', 'инспекционный орган'), ('other', 'иное')], max_length=1000)),
                ('working_with_ozakk', models.CharField(choices=[('less_one_year', 'Менее одного года'), ('more_one_year', 'Более одного года')], max_length=1000)),
                ('mark_our_service', models.PositiveIntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])),
                ('source_information', models.CharField(choices=[('web_site', 'через веб-сайт центра'), ('phone', ' по телефону'), ('facebook', 'страничка в Фейсбуке'), ('telegram', 'Телеграм канал'), ('friends', 'через знакомых'), ('other_source', 'иное')], max_length=1000)),
                ('mark_info_applicants', models.PositiveIntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])),
                ('mark_employee_attitude', models.CharField(choices=[('yes', 'да'), ('no', 'нет')], max_length=1000)),
                ('mark_deadline', models.PositiveIntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])),
                ('mark_competence_appraisers', models.PositiveIntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])),
                ('mark_objectivity_ozakk', models.PositiveIntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])),
                ('mark_confidentiality_ozakk', models.PositiveIntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])),
                ('trainings', models.TextField(null=True)),
                ('site_info', models.TextField(null=True)),
                ('offers', models.TextField(null=True)),
                ('questionnaire', models.CharField(choices=[('manager', 'руководитель органа по оценке соответствия'), ('employee', ' сотрудник органа по оценке соответствия'), ('other_employee', 'иное')], max_length=1000)),
            ],
        ),
    ]