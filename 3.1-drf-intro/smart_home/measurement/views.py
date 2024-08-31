# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView

from measurement.models import Sensor, Measurement
from measurement.serializers import SensorSerializer, MeasurementSerializer, MeasurementCreateSerializer


@api_view(['GET'])
def demo(request):
    data = {'message': 'Hello'}
    return Response(data)

class SensorsView(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

class UpdateSensorView(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

class MeasurementCreateSerializerView(CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementCreateSerializer