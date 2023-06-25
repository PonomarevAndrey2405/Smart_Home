from rest_framework.generics import RetrieveAPIView, ListAPIView
from rest_framework.response import Response

from measurement.models import Sensor, Measurement
from measurement.serializers import SensorDetailsSerializer, MeasurementsSerializer


class CreateAPIView(ListAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailsSerializer

    def post(self, request):
        review = SensorDetailsSerializer(data=request.data)
        if review.is_valid():
            review.save()

        return Response({'status': 'OK'})


class ListCreateAPIView(ListAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementsSerializer

    def post(self, request):
        review = MeasurementsSerializer(data=request.data)
        if review.is_valid():
            review.save()

        return Response({'status': 'OK'})


class RetrieveUpdateAPIView(RetrieveAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailsSerializer

    def patch(self, request, pk):
        sensor = Sensor.objects.get(pk=pk)
        serializer = SensorDetailsSerializer(sensor, data=request.data)
        if serializer.is_valid():
            serializer.save()

        return Response(serializer.data)


class ListView(ListAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailsSerializer

