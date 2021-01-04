from django.db import models


class CodeType(models.Model):
    name = models.CharField(max_length=500)

    def __str__(self):
        return self.name


# N60368 = '60368'

class Code(models.Model):
    N060001 = '060001'
    N060002 = '060002'
    N060025 = '060025'
    N060030 = '060030'
    N060031 = '060031'
    N060043 = '060043'
    N060047 = '060047'
    N060065 = '060065'
    N060080 = '060080'
    N060085 = '060085'
    N060128 = '060128'
    N060142 = '060142'
    N060157 = '060157'
    N060168 = '060168'
    N060170 = '060170'
    N060171 = '060171'
    N060173 = '060173'
    N060174 = '060174'
    N060176 = '060176'
    N060178 = '060178'
    N060192 = '060192'
    N060237 = '060237'
    N060241 = '060241'
    N060243 = '060243'
    N060247 = '060247'
    N060256 = '060256'
    N060275 = '060275'
    N060282 = '060282'
    N060294 = '060294'
    N060301 = '060301'
    N060319 = '060319'
    N060340 = '060340'
    N060344 = '060344'
    N060346 = '060346'
    N060348 = '060348'
    N060349 = '060349'
    N060352 = '060352'
    N060353 = '060353'
    N060354 = '060354'
    N060357 = '060357'
    N060361 = '060361'
    N060362 = '060362'
    N060369 = '060369'
    N060371 = '060371'
    N060373 = '060373'
    N060374 = '060374'
    N060376 = '060376'
    NMS0001 = 'ms0001'
    NMS0002 = 'ms0002'
    NMS0003 = 'ms0003'
    NMS0004 = 'ms0004'
    NMS0005 = 'ms0005'
    NMS0006 = 'ms0006'
    NMS0007 = 'ms0007'
    NMS0008 = 'ms0008'
    NMS0009 = 'ms0009'
    NMS0010 = 'ms0010'
    NMS0011 = 'ms0011'
    NMS0012 = 'ms0012'
    NMS0013 = 'ms0013'
    NMS0014 = 'ms0014'
    NMS0015 = 'ms0015'
    NMS0016 = 'ms0016'
    NMS0017 = 'ms0017'
    NMS0018 = 'ms0018'
    NMS0019 = 'ms0019'
    NMS0020 = 'ms0020'
    NMS0021 = 'ms0021'
    NMS0022 = 'ms0022'
    NMS0023 = 'ms0023'
    NMS0024 = 'ms0024'
    NMS0025 = 'ms0025'
    NMS0026 = 'ms0026'
    NMS0027 = 'ms0027'
    NMS0028 = 'ms0028'
    NMS0029 = 'ms0029'
    NMS0030 = 'ms0030'
    NMS0031 = 'ms0031'
    NMS0032 = 'ms0032'
    NMS0033 = 'ms0033'
    NMS0034 = 'ms0034'
    NMS0035 = 'ms0035'
    NMS0036 = 'ms0036'
    NMS0037 = 'ms0037'
    NMS0038 = 'ms0038'
    NMS0039 = 'ms0039'
    NMS0040 = 'ms0040'

    N060368 = '060368'
    N060366 = '060366'
    N060046 = '060046'
    N060378 = '060378'
    N060167 = '060167'

    STATUS_TYPES = (
        (N060001, '060001'),
        (N060002, '060002'),
        (N060025, '060025'),
        (N060030, '060030'),
        (N060031, '060031'),
        (N060043, '060043'),
        (N060047, '060047'),
        (N060065, '060065'),
        (N060080, '060080'),
        (N060085, '060085'),
        (N060128, '060128'),
        (N060142, '060142'),
        (N060157, '060157'),
        (N060168, '060168'),
        (N060170, '060170'),
        (N060171, '060171'),
        (N060173, '060173'),
        (N060174, '060174'),
        (N060176, '060176'),
        (N060178, '060178'),
        (N060192, '060192'),
        (N060237, '060237'),
        (N060241, '060241'),
        (N060243, '060243'),
        (N060247, '060247'),
        (N060256, '060256'),
        (N060275, '060275'),
        (N060282, '060282'),
        (N060301, '060301'),
        (N060319, '060319'),
        (N060340, '060340'),
        (N060344, '060344'),
        (N060346, '060346'),
        (N060348, '060348'),
        (N060349, '060349'),
        (N060352, '060352'),
        (N060353, '060353'),
        (N060354, '060354'),
        (N060357, '060357'),
        (N060361, '060361'),
        (N060362, '060362'),
        (N060369, '060369'),
        (N060371, '060371'),
        (N060373, '060373'),
        (N060374, '060374'),
        (N060368, '060368'),
        (N060366, '060366'),
        (N060167, '060167'),
        (N060376, '060376'),
        (N060378, '060378'),
        (N060046, '060046'),
        (N060294, '060294'),
        (NMS0001, 'ms0001'),
        (NMS0002, 'ms0002'),
        (NMS0003, 'ms0003'),
        (NMS0004, 'ms0004'),
        (NMS0005, 'ms0005'),
        (NMS0006, 'ms0006'),
        (NMS0007, 'ms0007'),
        (NMS0008, 'ms0008'),
        (NMS0009, 'ms0009'),
        (NMS0010, 'ms0010'),
        (NMS0011, 'ms0011'),
        (NMS0012, 'ms0012'),
        (NMS0013, 'ms0013'),
        (NMS0014, 'ms0014'),
        (NMS0015, 'ms0015'),
        (NMS0016, 'ms0016'),
        (NMS0017, 'ms0017'),
        (NMS0018, 'ms0018'),
        (NMS0019, 'ms0019'),
        (NMS0020, 'ms0020'),
        (NMS0021, 'ms0021'),
        (NMS0022, 'ms0022'),
        (NMS0023, 'ms0023'),
        (NMS0024, 'ms0024'),
        (NMS0025, 'ms0025'),
        (NMS0026, 'ms0026'),
        (NMS0027, 'ms0027'),
        (NMS0028, 'ms0028'),
        (NMS0029, 'ms0029'),
        (NMS0030, 'ms0030'),
        (NMS0031, 'ms0031'),
        (NMS0032, 'ms0032'),
        (NMS0033, 'ms0033'),
        (NMS0034, 'ms0034'),
        (NMS0035, 'ms0035'),
        (NMS0036, 'ms0036'),
        (NMS0037, 'ms0037'),
        (NMS0038, 'ms0038'),
        (NMS0039, 'ms0039'),
        (NMS0040, 'ms0040'),

    )

    cod_tnved = models.CharField(max_length=500)
    organ_number = models.CharField(max_length=50, choices=STATUS_TYPES)

    def __str__(self):
        return self.cod_tnved
