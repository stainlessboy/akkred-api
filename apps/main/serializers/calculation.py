from collections import defaultdict

from rest_framework import serializers


class CalculationSerializers(serializers.Serializer):
    type = serializers.CharField(write_only=True)
    calculation_type = serializers.CharField(write_only=True)
    number = serializers.IntegerField(write_only=True)
    number_inspection = serializers.IntegerField(write_only=True,
                                                 required=False)
    sum = serializers.DecimalField(max_digits=11, decimal_places=2,
                                   required=False)

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
                t = number / (480 / 12)
                if (t % 1) > 0 and (t % 1) <= 0.5:
                    bal = 0.5
                elif (t % 1) == 0:
                    bal = 0
                else:
                    bal = 1
                t = int(t) + bal
                num_day_total = t + 3
                sum = num_day_total * c
            if validated_data['calculation_type'] == 'site':
                t1 = (number / (480 / 18))
                if (t1 % 1) > 0 and (t1 % 1) <= 0.5:
                    bal = 0.5
                elif (t1 % 1) == 0:
                    bal = 0
                else:
                    bal = 1
                t1 = int(t1) + bal
                t2 = (number / 60)
                if (t2 % 1) > 0 and (t2 % 1) <= 0.5:
                    bal = 0.5
                elif (t2 % 1) == 0:
                    bal = 0
                else:
                    bal = 1
                t2 = int(t2) + bal
                num_day_total = t1 + t2 + 4
                sum = num_day_total * c

        # TODO expansion
        if validated_data['type'] == 'expansion':
            if validated_data['calculation_type'] == 'expertise':
                t = number / (480 / 12)
                if (t % 1) > 0 and (t % 1) <= 0.5:
                    bal = 0.5
                elif (t % 1) == 0:
                    bal = 0
                else:
                    bal = 1
                t = int(t) + bal
                num_day_total = t + 1
                sum = num_day_total * c
            if validated_data['calculation_type'] == 'site':
                t1 = (number / (480 / 18))
                if (t1 % 1) > 0 and (t1 % 1) <= 0.5:
                    bal = 0.5
                elif (t1 % 1) == 0:
                    bal = 0
                else:
                    bal = 1
                t1 = int(t1) + bal
                t2 = (number / 60)
                if (t2 % 1) > 0 and (t2 % 1) <= 0.5:
                    bal = 0.5
                elif (t2 % 1) == 0:
                    bal = 0
                else:
                    bal = 1
                t2 = int(t2) + bal
                num_day_total = t1 + t2 + 2
                sum = num_day_total * c

        # TODO actualization
        if validated_data['type'] == 'actualization':
            t = number / (480 / 2)
            if (t % 1) > 0 and (t % 1) <= 0.5:
                bal = 0.5
            elif (t % 1) == 0:
                bal = 0
            else:
                bal = 1
            t = int(t) + bal
            num_day_total = t + 1
            sum = num_day_total * c
        # TODO inspection_control
        if validated_data['type'] == 'inspection_control':
            t = number / 60
            if (t % 1) > 0 and (t % 1) <= 0.5:
                bal = 0.5
            elif (t % 1) == 0:
                bal = 0
            else:
                bal = 1
            t = int(t) + bal

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

            num_day_total = t + num_day_rec + 4
            sum = num_day_total * c

        validated_data.update(sum=sum)
        return validated_data
