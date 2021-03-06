# Generated by Django 2.1.2 on 2020-11-03 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0127_auto_20200917_1246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='code',
            name='organ_number',
            field=models.CharField(choices=[('060001', '060001'), ('060002', '060002'), ('060025', '060025'), ('060030', '060030'), ('060031', '060031'), ('060043', '060043'), ('060047', '060047'), ('060065', '060065'), ('060080', '060080'), ('060085', '060085'), ('060128', '060128'), ('060142', '060142'), ('060157', '060157'), ('060168', '060168'), ('060170', '060170'), ('060171', '060171'), ('060173', '060173'), ('060174', '060174'), ('060176', '060176'), ('060178', '060178'), ('060192', '060192'), ('060237', '060237'), ('060241', '060241'), ('060243', '060243'), ('060247', '060247'), ('060256', '060256'), ('060275', '060275'), ('060282', '060282'), ('060301', '060301'), ('060319', '060319'), ('060340', '060340'), ('060344', '060344'), ('060346', '060346'), ('060348', '060348'), ('060349', '060349'), ('060352', '060352'), ('060353', '060353'), ('060354', '060354'), ('060357', '060357'), ('060361', '060361'), ('060362', '060362'), ('060369', '060369'), ('060371', '060371'), ('060373', '060373'), ('060374', '060374'), ('060368', '060368'), ('060167', '060167'), ('060376', '060376'), ('060378', '060378'), ('ms0001', 'ms0001'), ('ms0002', 'ms0002'), ('ms0003', 'ms0003'), ('ms0004', 'ms0004'), ('ms0005', 'ms0005'), ('ms0006', 'ms0006'), ('ms0007', 'ms0007'), ('ms0008', 'ms0008'), ('ms0009', 'ms0009'), ('ms0010', 'ms0010'), ('ms0011', 'ms0011'), ('ms0012', 'ms0012'), ('ms0013', 'ms0013'), ('ms0014', 'ms0014'), ('ms0015', 'ms0015'), ('ms0016', 'ms0016'), ('ms0017', 'ms0017'), ('ms0018', 'ms0018'), ('ms0019', 'ms0019'), ('ms0020', 'ms0020'), ('ms0021', 'ms0021'), ('ms0022', 'ms0022'), ('ms0023', 'ms0023'), ('ms0024', 'ms0024'), ('ms0025', 'ms0025'), ('ms0026', 'ms0026'), ('ms0027', 'ms0027'), ('ms0028', 'ms0028'), ('ms0029', 'ms0029'), ('ms0030', 'ms0030'), ('ms0031', 'ms0031'), ('ms0032', 'ms0032'), ('ms0033', 'ms0033'), ('ms0034', 'ms0034'), ('ms0035', 'ms0035'), ('ms0036', 'ms0036'), ('ms0037', 'ms0037'), ('ms0038', 'ms0038'), ('ms0039', 'ms0039'), ('ms0040', 'ms0040')], max_length=50),
        ),
    ]
