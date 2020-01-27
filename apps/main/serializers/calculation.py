from collections import defaultdict

from rest_framework import serializers


class CalculationSerializers(serializers.Serializer):
    type = serializers.CharField(write_only=True)
    calculation_type = serializers.CharField(write_only=True)
    number = serializers.FloatField(write_only=True)
    sum = serializers.FloatField(required=False)

    def validate(self, attrs):
        errors = defaultdict(list)

        type = attrs.get('type', None)
        calculation_type = attrs.get('calculation_type', None)
        if type == 'actualization' and not calculation_type:
            errors['calculation_type'].append('Error')

        if errors:
            raise serializers.ValidationError(errors)

        return attrs

    def create(self, validated_data: dict):

        sum = 0
        c = 105000
        number = validated_data['number']

        # TODO accreditation
        if validated_data['type'] == 'accreditation':
            if validated_data['calculation_type'] == 'expertise':
                t = number / 20
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
                t = number / 20
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
                    sum = (time + 1 + (t / 32)) * c
                else:
                    time = t
                    sum = (time + 1 + (t / 32)) * c

        # TODO actualization
        if validated_data['type'] == 'actualization':
            t = number / 120
            if t <= 1:
                time = 0.5
                sum = (time + 0.5) * c
            else:
                time = t
                sum = (time + 0.5) * c
        validated_data.update(sum=sum)
        return validated_data
