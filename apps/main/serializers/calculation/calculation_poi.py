from collections import defaultdict

from rest_framework import serializers


class CalculationPoiSerializers(serializers.Serializer):
    type = serializers.CharField(write_only=True)
    calculation_type = serializers.CharField(write_only=True, required=False)
    number = serializers.FloatField(required=False)
    number2 = serializers.FloatField(required=False)
    number_inspection = serializers.FloatField(write_only=True, required=False)
    sum = serializers.FloatField(required=False)

    def validate(self, attrs):
        errors = defaultdict(list)

        type = attrs.get('type', None)
        calculation_type = attrs.get('calculation_type', None)
        num_test = attrs.get('number_inspection', None)
        number = attrs.get('number', None)
        number2 = attrs.get('number2', None)
        if type not in ['inspection_control',
                        'actualization'] and not calculation_type:
            errors['calculation_type'].append('Error')
        if type == 'inspection_control' and not num_test:
            errors['number_inspection'].append('Error')
        if type == 'inspection_control' and not number2:
            errors['number2'].append('Error')
        if type != 'inspection_control' and not number:
            errors['number'].append('Error')
        if errors:
            raise serializers.ValidationError(errors)
        return attrs

    def create(self, validated_data: dict):

        sum = 0
        c = 1050000
        number1 = validated_data.get('number', None)
        number2 = validated_data.get('number2', None)
        num_test = validated_data.get('number_inspection', None)

        # TODO accreditation
        if validated_data['type'] == 'accreditation':
            if validated_data['calculation_type'] == 'expertise':
                t = number1 / (480 / 15)

                num_day_total = t + 3
                num_day_total = round(num_day_total, 2)

                sum = num_day_total * c
            if validated_data['calculation_type'] == 'site':
                t = number1 / (480 / 30)

                num_day_total = t + 6
                num_day_total = round(num_day_total, 2)

                sum = num_day_total * c

        # TODO expansion
        if validated_data['type'] == 'expansion':
            if validated_data['calculation_type'] == 'expertise':
                t = number1 / (480 / 12)

                num_day_total = t + 1
                num_day_total = round(num_day_total, 2)

                sum = num_day_total * c
            if validated_data['calculation_type'] == 'site':
                t = number1 / (480 / 30)

                num_day_total = t + 4
                num_day_total = round(num_day_total, 2)

                sum = num_day_total * c

        # TODO actualization
        if validated_data['type'] == 'actualization':
            t = number1 / 480

            num_day_total = t + 1
            num_day_total = round(num_day_total, 2)

            sum = num_day_total * c
        # TODO inspection_control
        if validated_data['type'] == 'inspection_control':
            t = number2 / (480 / 30)

            if num_test <= 24:
                num_day_rec = 1.0
            elif num_test > 24 and num_test <= 48:
                num_day_rec = 2.0
            else:
                num_day_rec = 2 + (((num_test - 48) / 120) * 1)

            num_day_total = t + num_day_rec + 4
            num_day_total = round(num_day_total, 2)

            sum = num_day_total * c

        validated_data.update(sum=sum)
        return validated_data
