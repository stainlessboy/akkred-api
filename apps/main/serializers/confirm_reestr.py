from rest_framework import serializers

from main.models.confirm_reestr import ConfirmReestr


class ConfirmReestrModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConfirmReestr
        exclude = ['designation_of_the_fundamental_standard',
                   'region',
                   'directions',
                   'text',
                   'oked',
                   'soogu',
                   'type_ownership',
                   'title_yurd_lisa',
                   'qr_code',
                   ]
