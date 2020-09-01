from rest_framework import serializers


class CalculationOkSerializers(serializers.Serializer):
    type = serializers.CharField(write_only=True)
    number = serializers.FloatField(write_only=True)
    sum = serializers.FloatField(required=False)

    def create(self, validated_data: dict):

        sum = 0
        c = 1050000
        number1 = validated_data.get('number', None)

        # TODO Odobrenie
        if validated_data['type'] == 'Odobrenie':
            if number1 / (480 / 30) <= 1:
                t1 = 1
            else:
                t1 = number1 / (480 / 30)

            if number1 / (480 / 40) <= 1:
                t2 = 1
            else:
                t2 = number1 / (480 / 40)

            num_day_total = t1 + t2 + 1.5
            num_day_total = round(num_day_total, 2)

            sum = num_day_total * c

        # TODO expansion
        if validated_data['type'] == 'expansion':
            if number1 / (480 / 30) <= 1:
                t1 = 1
            else:
                t1 = number1 / (480 / 30)

            if number1 / (480 / 40) <= 1:
                t2 = 1
            else:
                t2 = number1 / (480 / 40)

            num_day_total = t1 + t2 + 1.5
            num_day_total = round(num_day_total, 2)

            sum = num_day_total * c

        # TODO actualization
        if validated_data['type'] == 'actualization':
            t = number1 / (480 / 2)

            num_day_total = t + 1
            num_day_total = round(num_day_total, 2)

            sum = num_day_total * c

        validated_data.update(sum=sum)
        return validated_data
