from rest_framework import viewsets, filters
from .models import Car
from .serializers import CarSerializer

class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'brand', 'model', 'price']
