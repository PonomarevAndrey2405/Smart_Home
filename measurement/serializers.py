from rest_framework import serializers

from measurement.models import Sensor, Measurement


class MeasurementsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['sensor_id', 'temperature', 'create_at']


class SensorDetailsSerializer(serializers.ModelSerializer):
    measurements = MeasurementsSerializer(read_only=True, many=True)
    class Meta:
        model = Sensor
        fields = ['id', 'title', 'discription', 'measurements']


class SensorChengeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ['discription']

