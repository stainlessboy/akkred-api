from django.db import models


class SatisfactionQuestionnaire(models.Model):
    TESTING_LABORATORY = 'testing_laboratory'
    CALIBRATION_LABORATORY = 'calibration_laboratory'
    POV_CALIBRATION_LABORATORY = 'pov_calibration_laboratory'
    MEDICAL_LABORATORY = 'medical_laboratory'
    PRODUCT_CERTIFICATION_BODY = 'product_certification_body'
    AUTHORITY_FOR_CERTIFICATION_OF_SERVICES = 'authority_for_certification_of_services'
    MANAGEMENT_SYSTEM_CERTIFICATION_BODY = 'management_system_certification_body'
    PERSONNEL_CERTIFICATION_BODY = 'personnel_certification_body'
    INSPECTION_BODY = 'inspection_body'
    OTHER = 'other'

    TYPES_OF_ACTIVITY = (
        (TESTING_LABORATORY, 'испытательная лаборатория'),
        (CALIBRATION_LABORATORY, 'калибровочная лаборатория'),
        (POV_CALIBRATION_LABORATORY, 'поверочная лаборатория'),
        (MEDICAL_LABORATORY, 'медицинская лаборатория'),
        (PRODUCT_CERTIFICATION_BODY, 'орган по сертификации продукции'),
        (AUTHORITY_FOR_CERTIFICATION_OF_SERVICES, 'орган по сертификации услуг'),
        (MANAGEMENT_SYSTEM_CERTIFICATION_BODY, 'орган по сертификации систем менеджмента'),
        (PERSONNEL_CERTIFICATION_BODY, 'орган по сертификации персонала'),
        (INSPECTION_BODY, 'инспекционный орган'),
        (OTHER, 'иное'),
    )

    LESS_ONE_YEAR = 'less_one_year'
    MORE_ONE_YEAR = 'more_one_year'

    WORKING_TYPES = (
        (LESS_ONE_YEAR, 'Менее одного года'),
        (MORE_ONE_YEAR, 'Более одного года'),
    )

    YES = 'yes'
    NO = 'no'

    EMPLOYEE_ATTITUDE_TYPES = (
        (YES, 'да'),
        (NO, 'нет'),
    )

    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5

    MARK = (
        (ONE, '1'),
        (TWO, '2'),
        (THREE, '3'),
        (FOUR, '4'),
        (FIVE, '5'),
    )

    WEB_SITE = 'web_site'
    PHONE = 'phone'
    FACEBOOK = 'facebook'
    TELEGRAM = 'telegram'
    FRIENDS = 'friends'
    OTHER_SOURCE = 'other_source'

    SOURCE_TYPES = (
        (WEB_SITE, 'через веб-сайт центра'),
        (PHONE, ' по телефону'),
        (FACEBOOK, 'страничка в Фейсбуке'),
        (TELEGRAM, 'Телеграм канал'),
        (FRIENDS, 'через знакомых'),
        (OTHER_SOURCE, 'иное'),
    )

    MANAGER = 'manager'
    EMPLOYEE = 'employee'
    OTHER_EMPLOYEE = 'other_employee'

    QUESTIONNAIRE_TYPES = (
        (MANAGER, 'руководитель органа по оценке соответствия'),
        (EMPLOYEE, ' сотрудник органа по оценке соответствия'),
        (OTHER_EMPLOYEE, 'иное'),
    )

    type_of_activity = models.CharField(choices=TYPES_OF_ACTIVITY, max_length=1000)
    working_with_ozakk = models.CharField(choices=WORKING_TYPES, max_length=1000)
    mark_our_service = models.PositiveIntegerField(choices=MARK)
    source_information = models.CharField(choices=SOURCE_TYPES, max_length=1000)
    mark_info_applicants = models.PositiveIntegerField(choices=MARK)
    mark_employee_attitude = models.CharField(max_length=1000, choices=EMPLOYEE_ATTITUDE_TYPES)
    mark_deadline = models.PositiveIntegerField(choices=MARK)
    mark_competence_appraisers = models.PositiveIntegerField(choices=MARK)
    mark_objectivity_ozakk = models.PositiveIntegerField(choices=MARK)
    mark_confidentiality_ozakk = models.PositiveIntegerField(choices=MARK)
    trainings = models.TextField(null=True)
    site_info = models.TextField(null=True)
    offers = models.TextField(null=True)
    questionnaire = models.CharField(choices=QUESTIONNAIRE_TYPES, max_length=1000)

    def __str__(self):
        return self.questionnaire
