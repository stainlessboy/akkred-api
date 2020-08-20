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

    def to_representation(self, instance):
        self.fields['reissue_date'] = serializers.DateField(
            format="%d.%m.%Y")
        self.fields['accreditation_date'] = serializers.DateField(
            format="%d.%m.%Y")
        self.fields['validity_date'] = serializers.DateField(
            format="%d.%m.%Y")
        self.fields['status_date'] = serializers.DateField(
            format="%d.%m.%Y")
        return super().to_representation(instance)
