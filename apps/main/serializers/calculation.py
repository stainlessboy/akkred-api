from collections import defaultdict

from rest_framework import serializers


class CalculationSerializers(serializers.Serializer):
    type = serializers.CharField(write_only=True)
    calculation_type = serializers.CharField(write_only=True)
    number = serializers.FloatField(write_only=True)
    number_inspection = serializers.FloatField(write_only=True, required=False)
    sum = serializers.FloatField(required=False)

    def validate(self, attrs):
        errors = defaultdict(list)

        type = attrs.get('type', None)
        calculation_type = attrs.get('calculation_type', None)
        num_test = attrs.get('number_inspection', None)
        if type == 'actualization' and not calculation_type:
            errors['calculation_type'].append('Error')
        if type == 'inspection_control' and not num_test:
            errors['number_inspection'].append('Error')
        if errors:
            raise serializers.ValidationError(errors)
        return attrs

    def create(self, validated_data: dict):

        sum = 0
        c = 1050000
        number = validated_data['number']
        num_test = validated_data.get('number_inspection', None)

        # TODO accreditation
        if validated_data['type'] == 'accreditation':
            if validated_data['calculation_type'] == 'expertise':
                t = number / 40
                if t <= 1:
                    time = 0.5
                    sum = (time + 2) * c
                else:
                    time = t
                    sum = (time + 2) * c
            if validated_data['calculation_type'] == 'site':
                t = number / 50
                if t <= 1:
                    time = 1
                    sum = (time + 2 + (t / 32)) * c
                else:
                    time = t
                    sum = (time + 2 + (t / 32)) * c
        # TODO expansion
        if validated_data['type'] == 'expansion':
            if validated_data['calculation_type'] == 'expertise':
                t = number / 40
                if t <= 1:
                    time = 0.5
                    sum = time * c
                else:
                    time = t
                    sum = time * c
            if validated_data['calculation_type'] == 'site':
                t = number / 50
                if t <= 1:
                    time = 1
                    sum = (time + 1 + (t / 28.24)) * c
                else:
                    time = t
                    sum = (time + 1 + (t / 28.24)) * c

        # TODO actualization
        if validated_data['type'] == 'actualization':
            t = number / 240
            if t <= 1:
                time = 0.5
                sum = (time + 0.5) * c
            else:
                time = t
                sum = (time + 0.5) * c
        # TODO inspection_control
        if validated_data['type'] == 'inspection_control':
            t = number / 10

            from math import ceil

            if num_test <= 200:
                num_day_rec = 1.5
            elif num_test > 200 and num_test <= 500:
                num_day_rec = 2.0
            elif num_test > 500 and num_test <= 1000:
                num_day_rec = 2.5
            elif num_test > 1000 and num_test <= 2000:
                num_day_rec = 3.0
            elif num_test > 2000 and num_test <= 3500:
                num_day_rec = 3.5
            elif num_test > 3500 and num_test <= 5500:
                num_day_rec = 4.0
            elif num_test > 550 and num_test <= 8000:
                num_day_rec = 4.5
            else:
                num_day_rec = 4.5 + ceil((num_test - 8000) / 3000) / 2

            print(num_day_rec)

            if t <= 1:
                time = 1
                sum = (time + 0.5 + num_day_rec) * c
            else:
                time = t
                sum = (time + 0.5 + num_day_rec) * c
        validated_data.update(sum=sum)
        return validated_data
