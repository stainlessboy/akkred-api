from collections import defaultdict

from rest_framework import serializers


class CalculationOspersSerializers(serializers.Serializer):
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
        if type != 'actualization' and not number2:
            errors['number2'].append('Error')
        if type != 'inspection_control' and not number:
            errors['number2'].append('Error')
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
                t = number1 / (480 / 10) + number2 / (480 / 30)

                num_day_total = t + 3
                num_day_total = round(num_day_total, 2)

                sum = num_day_total * c
            if validated_data['calculation_type'] == 'site':
                t = number1 / (480 / 60) + number2 / (480 / 120)

                num_day_total = t + 6
                num_day_total = round(num_day_total, 2)

                sum = num_day_total * c

        # TODO expansion
        if validated_data['type'] == 'expansion':
            if validated_data['calculation_type'] == 'expertise':
                t = number1 / (480 / 10) + number2 / (480 / 30)

                num_day_total = t + 1
                num_day_total = round(num_day_total, 2)

                sum = num_day_total * c
            if validated_data['calculation_type'] == 'site':
                t = number1 / (480 / 60) + number2 / (480 / 120)

                num_day_total = t + 4
                num_day_total = round(num_day_total, 2)

                sum = num_day_total * c

        # TODO actualization
        if validated_data['type'] == 'actualization':
            t = number1 / (480 / 2)

            num_day_total = t + 1
            num_day_total = round(num_day_total, 2)

            sum = num_day_total * c
        # TODO inspection_control
        if validated_data['type'] == 'inspection_control':
            t = number2 / 120

            from math import ceil
            if num_test <= 200:
                num_day_rec = 2
            elif num_test > 200 and num_test <= 500:
                num_day_rec = 3
            elif num_test > 500 and num_test <= 1000:
                num_day_rec = 4
            elif num_test > 1000 and num_test <= 2000:
                num_day_rec = 5
            elif num_test > 2000 and num_test <= 3500:
                num_day_rec = 6
            elif num_test > 3500 and num_test <= 5500:
                num_day_rec = 7
            elif num_test > 5500 and num_test <= 8000:
                num_day_rec = 8
            else:
                num_day_rec = 8 + ceil((num_test - 8000) / 3000)

            num_day_total = t + num_day_rec + 4
            num_day_total = round(num_day_total, 2)

            sum = num_day_total * c

        validated_data.update(sum=sum)
        return validated_data
