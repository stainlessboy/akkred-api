from rest_framework import permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

# external = True,
from main.models import Document, CategoryDocumentForm


class LanguageViewSet(GenericViewSet):
    url = 'http://akkred.uz:8081/'

    @action(['GET'], detail=False, permission_classes=[permissions.AllowAny])
    def menu(self, request):
        document = Document.objects.filter(id=89)[0]
        all_forms = document.document_forms.all()

        # TODO: Метрологические службы
        # TODO: Метрологические службы/лаборатории, проводящие калибровку средств измерений
        metro_one = all_forms.filter(category=2)
        form_list_metro_one = list()
        if metro_one:

            for form in metro_one:
                form_list_metro_one.append(dict(
                    title_ru=form.title,
                    title_en=form.title,
                    title_uz=form.title,
                    # url=form.file,
                    url=str('http://akkred.uz:8081/media/' + str(form.file)),
                    external=True,

                ))

        # TODO: Метрологические службы/лаборатории, проводящие поверку средств измерений
        metro_two = all_forms.filter(category=12)
        form_list_metro_two = list()
        if metro_two:

            for form in metro_two:
                form_list_metro_two.append(dict(
                    title_ru=form.title,
                    title_en=form.title,
                    title_uz=form.title,
                    # url=form.file,
                    url=str('http://akkred.uz:8081/media/' + str(form.file)),
                    external=True,

                ))

        # TODO: Метрологические службы/лаборатории, проводящие аттестацию МВИ
        metro_three = all_forms.filter(category=13)
        form_list_metro_three = list()
        if metro_three:

            for form in metro_three:
                form_list_metro_three.append(dict(
                    title_ru=form.title,
                    title_en=form.title,
                    title_uz=form.title,
                    url=str('http://akkred.uz:8081/media/' + str(form.file)),
                    external=True,

                ))

        # TODO: Метрологические службы/лаборатории, проводящие аттестацию СО
        metro_four = all_forms.filter(category=14)
        form_list_metro_four = list()
        if metro_four:
            for form in metro_four:
                form_list_metro_four.append(dict(
                    title_ru=form.title,
                    title_en=form.title,
                    title_uz=form.title,
                    url=str('http://akkred.uz:8081/media/' + str(form.file)),
                    external=True,

                ))

        # TODO: Для лабораторий
        # TODO: Органы по сертификации продукции
        organ_product = all_forms.filter(category=8)
        form_list_organ_product = list()
        if organ_product:

            for form in organ_product:
                form_list_organ_product.append(dict(
                    title_ru=form.title,
                    title_en=form.title,
                    title_uz=form.title,
                    url=str('http://akkred.uz:8081/media/' + str(form.file)),
                    external=True,

                ))

        # TODO: Органы по сертификации систем менеджмента
        organ_system_manage = all_forms.filter(category=9)
        form_list_organ_system_manage = list()
        if organ_system_manage:

            for form in organ_system_manage:
                form_list_organ_system_manage.append(dict(
                    title_ru=form.title,
                    title_en=form.title,
                    title_uz=form.title,
                    url=str('http://akkred.uz:8081/media/' + str(form.file)),
                    external=True,

                ))

        # TODO: Органы по сертификации персонала
        personal = all_forms.filter(category=10)
        form_list_personal = list()
        if personal:

            for form in personal:
                form_list_personal.append(dict(
                    title_ru=form.title,
                    title_en=form.title,
                    title_uz=form.title,
                    url=str('http://akkred.uz:8081/media/' + str(form.file)),
                    external=True,

                ))

        # TODO: Для лабораторий
        laboratories = all_forms.filter(category=1)
        form_list_laboratories = list()
        if laboratories:

            for form in laboratories:
                form_list_laboratories.append(dict(
                    title_ru=form.title,
                    title_en=form.title,
                    title_uz=form.title,
                    url=str('http://akkred.uz:8081/media/' + str(form.file)),
                    external=True,

                ))

        # TODO: Для инспекционных органов
        inspection = all_forms.filter(category=11)
        form_list_inspection = list()
        if inspection:

            for form in inspection:
                form_list_inspection.append(dict(
                    title_ru=form.title,
                    title_en=form.title,
                    title_uz=form.title,
                    url=str('http://akkred.uz:8081/media/' + str(form.file)),
                    external=True,

                ))

        # TODO: Для провайдеров программ проверки квалификации
        provid_program = all_forms.filter(category=3)
        form_list_provid_program = list()
        if provid_program:

            for form in provid_program:
                form_list_provid_program.append(dict(
                    title_ru=form.title,
                    title_en=form.title,
                    title_uz=form.title,
                    url=str('http://akkred.uz:8081/media/' + str(form.file)),
                    external=True,

                ))

        results = [
            # TODO: О нас
            dict(
                title_en='Biz haqimizda',
                title_ru='О нас',
                title_uz='Biz haqimizda',

                children=[
                    dict(
                        url='/static/about',
                        title_en='Akkreditatsiya toʻgʻrisida',
                        title_uz='Akkreditatsiya toʻgʻrisida',
                        title_ru='Об аккредитации',

                    ),
                    dict(
                        url='/static/center',
                        title_en='Markaz haqida',
                        title_uz='Markaz haqida',
                        title_ru='О Центре',

                    ),
                    dict(
                        url='/static/financing',
                        title_ru='Информация об источниках финансирования',
                        title_en='Moliyalashtirish manbalari toʻgʻrisida maʻlumot',
                        title_uz='Moliyalashtirish manbalari toʻgʻrisida maʻlumot',

                    ),
                    dict(
                        url='/static/rightsObligations',
                        title_ru='Права и обязанности органа по аккредитации',
                        title_en='Akkreditatsiya organining huquqlari va majburiyatlari',
                        title_uz='Akkreditatsiya organining huquqlari va majburiyatlari',
                    ),
                    dict(
                        url='/static/structure',
                        title_ru='Организационная структура',
                        title_en='Tashkiliy tuzilma',
                        title_uz='Tashkiliy tuzilma',
                    ),
                    dict(
                        url='/management',
                        title_ru='Руководство',
                        title_en='Rahbariyat',
                        title_uz='Rahbariyat',
                    ),
                    dict(
                        url='/static/advice',
                        title_ru='Совет по аккредитации',
                        title_en='Akkreditatsiya boʻyicha kengashi',
                        title_uz='Akkreditatsiya boʻyicha kengashi',
                    ),
                    dict(
                        title_ru='Технические комитеты',
                        title_en='Tehnik qoʻmitalar',
                        title_uz='Tehnik qoʻmitalar',
                        children=[
                            dict(
                                url='/static/techMain',
                                title_ru='О технических комитетах',
                                title_en='О технических комитетах',
                                title_uz='О технических комитетах',

                            ),
                            dict(
                                url='/static/tech5',
                                title_ru='Технический комитет «Метрология»',
                                title_en='Технический комитет «Метрология»',
                                title_uz='Технический комитет «Метрология»',
                            ),
                            dict(
                                url='/static/tech1',
                                title_ru='Технический комитет по испытательным лабораториям',
                                title_en='Sinov laboratoriyalari boʻyicha tehnik qoʻmita',
                                title_uz='Sinov laboratoriyalari boʻyicha tehnik qoʻmita',
                            ),
                        ]
                    ),
                    dict(
                        url='/static/anti-corruption',
                        title_ru='Противодействие коррупции',
                        title_en='Korrupsiyaga qarshi kurashish',
                        title_uz='Korrupsiyaga qarshi kurashish',
                    ),
                    # dict(
                    #     url='',
                    #     title_ru='',
                    #     title_en='',
                    #     title_uz='',
                    # )

                ],

            ),

            # TODO: Деятельность

            dict(
                title_ru='Деятельность',
                title_en='Faoliyat',
                title_uz='Faoliyat',
                children=[
                    dict(
                        title_ru='Проверка квалификации',
                        title_en='Malakani tekshirish',
                        title_uz='Malakani tekshirish',
                        children=[
                            dict(
                                url='/static/qualification1',
                                title_ru='Что такое проверка квалификации и для чего она нужна?',
                                title_en='Malakani tekshirish nima va u nima uchun kerak?',
                                title_uz='Malakani tekshirish nima va u nima uchun kerak?',
                            ),
                            dict(
                                url='/static/qualification2',
                                title_ru='Политика Центра по аккредитации в отношении участия заявителей и аккредитованных лабораторий в проверках квалификации',
                                title_en='Akkreditatsiya markazining ariza beruvchilar va akkreditatsiya qilingan laboratoriyalarning malakalarini tekshirishda ishtirok etishiga oid siyosati',
                                title_uz='Akkreditatsiya markazining ariza beruvchilar va akkreditatsiya qilingan laboratoriyalarning malakalarini tekshirishda ishtirok etishiga oid siyosati',
                            ),
                            dict(
                                url='/static/qualification3',
                                title_ru='Информация об аккредитованных провайдерах проверки квалификации в Республике Узбекистан',
                                title_en='Oʻzbekiston Respublikasida akkreditatsiya qilingan malakani tekshiruvchi provayderlar toʻgʻrisida ma’lumot',
                                title_uz='Oʻzbekiston Respublikasida akkreditatsiya qilingan malakani tekshiruvchi provayderlar toʻgʻrisida ma’lumot',
                            ),
                            dict(
                                url='/static/qualification4',
                                title_ru='Информация о провайдерах и программах проверки квалификации зарубежных стран',
                                title_en='Xorijiy mamlakatlarning malakani tekshiruvchi provayderlari va dasturlari haqida ma’lumot',
                                title_uz='Xorijiy mamlakatlarning malakani tekshiruvchi provayderlari va dasturlari haqida ma’lumot',
                            )

                        ]

                    ),
                    dict(
                        url='/static/international',
                        title_ru='Сотрудничество',
                        title_en='Hamkorlik',
                        title_uz='Hamkorlik',
                    ),
                    # dict(
                    #     url='/news',
                    #     title_ru='Все новости',
                    #     title_en='Barcha yangiliklar',
                    #     title_uz='Barcha yangiliklar',
                    # )

                ]

            ),

            # TODO: Документация
            dict(
                title_ru='Документация',
                title_en='Hujjatlar',
                title_uz='Hujjatlar',
                children=[
                    # dict(
                    #     url='/documents?parents=1',
                    #     title_ru='Документы Центра',
                    #     title_en='Markaz hujjatlari',
                    #     title_uz='Markaz hujjatlari',
                    #
                    # ),
                    dict(
                        url='/documents?parents=3',
                        title_ru='Нормативно-правовые акты',
                        title_en='Normativ-huquqiy hujjatlar',
                        title_uz='Normativ-huquqiy hujjatlar',

                    ),
                    dict(
                        title_ru='Документы Центра',
                        title_en='Markaz hujjatlari',
                        title_uz='Markaz hujjatlari',
                        children=[
                            dict(
                                url='/documents?parents=1',
                                title_ru='Документы аккредитации',
                                title_en='Akkreditasiya hujjatlari',
                                title_uz='Akkreditasiya hujjatlari',
                            ),
                            dict(
                                url='/documents?parents=7',
                                title_ru='Документы одобрения',
                                title_en='Ma`qullash hujjatlari',
                                title_uz='Ma`qullash hujjatlari',
                            )

                        ]
                    ),
                    dict(
                        title_ru='Международные документы',
                        title_en='Xalqaro hujjatlar',
                        title_uz='Xalqaro hujjatlar',
                        children=[
                            dict(
                                url='https://www.iaf.nu/articles/Mandatory_Documents_/38',
                                title_ru='Документы IAF',
                                title_en='IAF hujjatlarF',
                                title_uz='IAF hujjatlari',
                                external=True,
                            ),
                            dict(
                                url='https://ilac.org/publications-and-resources/',
                                title_ru='Документы ILAC',
                                title_en='ILAC hujjatlari',
                                title_uz='ILAC hujjatlari',
                                external=True,
                            )

                        ]
                    ),

                ]

            ),

            # TODO: Информация
            dict(
                title_ru='Информация',
                title_en='Ma`lumotlar',
                title_uz='Ma`lumotlar',
                children=[
                    dict(
                        title_ru='Общая информация по схемам аккредитации',
                        title_en='Akkreditatsiya sxemalari haqida umumiy maʻlumot',
                        title_uz='Akkreditatsiya sxemalari haqida umumiy maʻlumot',
                        children=[
                            dict(
                                url='/static/service1',
                                title_ru='Органы по сертификации продукции по OʻzDSt ISO/IEC 17065',
                                title_en='OʻzDSt ISO/IEC 17065 boʻyicha sertifikatlashtirish organlari',
                                title_uz='OʻzDSt ISO/IEC 17065 boʻyicha sertifikatlashtirish organlari',
                            ),
                            dict(
                                url='/static/service2',
                                title_ru='Органы по сертификации систем менеджмента по OʻzDSt ISO/IEC 17021',
                                title_en='OʻzDSt ISO / IEC 17021 boʻyicha menejment tizimlarini sertifikatlash organlari',
                                title_uz='OʻzDSt ISO / IEC 17021 boʻyicha menejment tizimlarini sertifikatlash organlari',
                            ),
                            dict(
                                url='/static/service3',
                                title_ru='Органы по сертификации персонала по OʻzDSt ISO/IEC 17024',
                                title_en='OʻzDSt ISO / IEC 17024 boʻyicha xodimlarni sertifikatlashtirish organlari',
                                title_uz='OʻzDSt ISO / IEC 17024 boʻyicha xodimlarni sertifikatlashtirish organlari',
                            ),
                            dict(
                                url='/static/service4',
                                title_ru='Испытательные лаборатории по OʻzDSt ISO/IEC 17025',
                                title_en='OʻzDSt ISO / IEC 17025 boʻyicha sinov laboratoriyalari',
                                title_uz='OʻzDSt ISO / IEC 17025 boʻyicha sinov laboratoriyalari',
                            ),
                            dict(
                                url='/static/service5',
                                title_ru='Инспекционные органы по OʻzDSt ISO/IEC 17020 ',
                                title_en='OʻzDSt ISO / IEC 17020 boʻyicha inspeksiya organlari',
                                title_uz='OʻzDSt ISO / IEC 17020 boʻyicha inspeksiya organlari',
                            ),
                            dict(
                                url='/static/service6',
                                title_ru='Провайдеры программ проверки квалификации по OʻzDSt ISO/IEC 17043',
                                title_en='OʻzDSt ISO / IEC 17043 boʻyicha malakani tekshirish dasturlari provayderlari',
                                title_uz='OʻzDSt ISO / IEC 17043 boʻyicha malakani tekshirish dasturlari provayderlari',
                            )

                        ]
                    ),
                    dict(
                        url='/inspection',
                        title_ru='Инспекционный контроль',
                        title_en='Inspeksiya nazorati',
                        title_uz='Inspeksiya nazorati',
                    ),
                    dict(
                        url='/registry-info',
                        title_ru='Информация о приостановленных, прекращенных и возобновленных свидетельствах об аккредитации',
                        title_en='Amal qilishi muddati toʻxtatib qoʻyilgan, tugatilgan va qayta tiklangan akkreditatsiya guvohnomalari toʻgʻrisida maʻlumot',
                        title_uz='Amal qilishi muddati toʻxtatib qoʻyilgan, tugatilgan va qayta tiklangan akkreditatsiya guvohnomalari toʻgʻrisida maʻlumot',
                    ),
                    dict(
                        url='/reestr',
                        title_ru='Государственный реестр аккредитованных ООС и МС',
                        title_en='Akkreditatsiya qilingan MBO va MX davlat reestri',
                        title_uz='Akkreditatsiya qilingan MBO va MX davlat reestri',
                    ),

                    dict(
                        url='/news',
                        title_ru='Все новости',
                        title_en='Barcha yangiliklar',
                        title_uz='Barcha yangiliklar',
                    ),
                    dict(
                        url='/reestr-confirm',
                        # title_ru='Texnik jihatdan malakaliligi maʼqullangan sinov laboratoriyalarining reestri',
                        # title_en='Texnik jihatdan malakaliligi maʼqullangan sinov laboratoriyalarining reestri',
                        title_uz='Texnik jihatdan malakaliligi maʼqullangan sinov laboratoriyalarining reestri',
                    ),

                ]

            ),
            dict(
                title_ru='Обратная связь',
                title_en='Qayta aloqa',
                title_uz='Qayta aloqa',
                children=[
                    dict(
                        url='/contacts',
                        title_ru='Контакты',
                        title_en='Aloqa ma`lumotlari',
                        title_uz='Aloqa ma`lumotlari',
                    ),
                    dict(
                        url='/satisfaction-rating',
                        title_ru='Оценка удовлетворенности',
                        title_en='Mijozlarning qoniqish darajasini baholash',
                        title_uz='Mijozlarning qoniqish darajasini baholash',
                    )

                ]

            ),
            dict(
                title_ru='Подача заявки',
                title_en='Buyurtma taqdim etish',
                title_uz='Buyurtma taqdim etish',
                children=[
                    dict(
                        title_ru='Для органов по сертификации',
                        title_en='Для органов по сертификации',
                        title_uz='Для органов по сертификации',
                        children=[
                            dict(
                                title_ru=' Органы по сертификации продукции',
                                title_en=' Органы по сертификации продукции',
                                title_uz=' Органы по сертификации продукции',
                                children=form_list_organ_product
                            ),
                            dict(
                                title_ru='Органы по сертификации систем менеджмента',
                                title_en='Органы по сертификации систем менеджмента',
                                title_uz='Органы по сертификации систем менеджмента',
                                children=form_list_organ_system_manage
                            ),
                            dict(
                                title_ru='Органы по сертификации персонала',
                                title_en='Органы по сертификации персонала',
                                title_uz='Органы по сертификации персонала',
                                children=form_list_personal
                            ),

                        ]
                    ),

                    dict(
                        title_ru='Для провайдеров программ проверки квалификации',
                        title_en='Для провайдеров программ проверки квалификации',
                        title_uz='Для провайдеров программ проверки квалификации',
                        children=form_list_provid_program
                    ),
                    dict(
                        title_ru='Для лабораторий',
                        title_en='Для лабораторий',
                        title_uz='Для лабораторий',
                        children=form_list_laboratories
                    ),
                    dict(
                        title_ru='Для инспекционных органов',
                        title_en='Для инспекционных органов',
                        title_uz='Для инспекционных органов',
                        children=form_list_inspection
                    ),
                    dict(
                        title_ru='Метрологические службы',
                        title_en='Метрологические службы',
                        title_uz='Метрологические службы',
                        children=[
                            dict(
                                title_ru=' Метрологические службы/лаборатории, проводящие калибровку средств измерений',
                                title_en=' Метрологические службы/лаборатории, проводящие калибровку средств измерений',
                                title_uz=' Метрологические службы/лаборатории, проводящие калибровку средств измерений',
                                children=form_list_metro_one
                            ),
                            dict(
                                title_ru='Метрологические службы/лаборатории, проводящие поверку средств измерений',
                                title_en='Метрологические службы/лаборатории, проводящие поверку средств измерений',
                                title_uz='Метрологические службы/лаборатории, проводящие поверку средств измерений',
                                children=form_list_metro_two
                            ),
                            dict(
                                title_ru='Метрологические службы/лаборатории, проводящие аттестацию МВИ',
                                title_en='Метрологические службы/лаборатории, проводящие аттестацию МВИ',
                                title_uz='Метрологические службы/лаборатории, проводящие аттестацию МВИ',
                                children=form_list_metro_three
                            ),
                            dict(
                                title_ru='Метрологические службы/лаборатории, проводящие аттестацию СО',
                                title_en='Метрологические службы/лаборатории, проводящие аттестацию СО',
                                title_uz='Метрологические службы/лаборатории, проводящие аттестацию СО',
                                children=form_list_metro_four
                            ),
                        ]
                    ),
                    dict(
                        url='/calculate',
                        title_ru='Расчет стоимости работ по аккредитации',
                        title_en='Akkreditatsiya boʻyicha ishlar narhini hisoblash',
                        title_uz='Akkreditatsiya boʻyicha ishlar narhini hisoblash',
                    ),

                ]
            ),

        ]
        return Response(dict(
            status=status.HTTP_200_OK, data=results
        ))
