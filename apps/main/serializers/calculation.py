from collections import defaultdict
from math import ceil

from rest_framework import serializers


def fixProblems(value):
    if (value <= 200):
        return 1
    elif (value <= 500):
        return 2
    else:
        return 3


# Функция для ИК

def numberRec(value):
    if value <= 200:
        return 1.5
    elif value <= 500:
        return 2.0
    elif value <= 1000:
        return 2.5
    elif value <= 2000:
        return 3.0
    elif value <= 3500:
        return 3.5
    elif value <= 5500:
        return 4.0
    elif value <= 8000:
        return 4.5
    else:
        return 4.5 + ceil((value - 8000) / 3000) / 2

class CalculationSerializers(serializers.Serializer):
    type = serializers.CharField(write_only=True)
    calculation_type = serializers.CharField(write_only=True, required=False)
    number = serializers.FloatField(write_only=True)
    number_inspection = serializers.FloatField(write_only=True, required=False)
    sum = serializers.FloatField(required=False)

    def validate(self, attrs):
        errors = defaultdict(list)

        type = attrs.get('type', None)
        calculation_type = attrs.get('calculation_type', None)
        num_test = attrs.get('number_inspection', None)
        if type not in ['inspection_control',
                        'actualization'] and not calculation_type:
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

        # TODO accreditation // входные данные - numPos
        if validated_data['type'] == 'accreditation':
            if validated_data['calculation_type'] == 'expertise':
                t = (number / 40)
                num_day_total = t + 3
                num_day_total = round(num_day_total, 2)

                sum = num_day_total * c
            if validated_data['calculation_type'] == 'site':
                t1 = (number / 26.67)
                t2 = (number / 60)
                t3 = fixProblems(number)
                num_day_total = t1 + t2 + t3 + 4
                num_day_total = round(num_day_total, 2)

                sum = num_day_total * c

        # TODO expansion // входные данные - numND
        if validated_data['type'] == 'expansion':
            if validated_data['calculation_type'] == 'expertise':
                t = (number / 40)
                num_day_total = t + 1
                num_day_total = round(num_day_total, 2)

                sum = num_day_total * c
            if validated_data['calculation_type'] == 'site':
                t1 = (number / 26.67)
                t2 = (number / 60)
                t3 = fixProblems(number)
                num_day_total = t1 + t2 + t3 + 2
                num_day_total = round(num_day_total, 2)

                sum = num_day_total * c

        # TODO actualization // входные данные - numND
        if validated_data['type'] == 'actualization':
            t = (number / 240)
            num_day_total = t + 1
            num_day_total = round(num_day_total, 2)

            sum = num_day_total * c
        # TODO inspection_control // входные данные - numND, num_test
        if validated_data['type'] == 'inspection_control':
            t1 = (number / 60)
            t2 = numberRec(num_test)
            num_day_total = t1 + t2 + 4
            num_day_total = round(num_day_total, 2)

            sum = num_day_total * c

        validated_data.update(sum=sum)
        return validated_data
