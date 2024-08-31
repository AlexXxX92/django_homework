from django.urls import path

from measurement.views import SensorsView, UpdateSensorView, MeasurementCreateSerializerView

urlpatterns = [
    path('sensors/', SensorsView.as_view()),
    path('sensors/<pk>/', UpdateSensorView.as_view()),
    path('measurements/', MeasurementCreateSerializerView.as_view()),
    # TODO: зарегистрируйте необходимые маршруты
]
