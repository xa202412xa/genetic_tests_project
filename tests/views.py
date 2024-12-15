from rest_framework import generics
from django.db import models
from .models import GeneticTest
from .serializers import GeneticTestSerializer
from rest_framework.response import Response


class GeneticTestListCreate(generics.ListCreateAPIView):
    queryset = GeneticTest.objects.all()
    serializer_class = GeneticTestSerializer

class GeneticTestListBySpecies(generics.ListAPIView):
    serializer_class = GeneticTestSerializer

    def get_queryset(self):
        species = self.request.query_params.get('species')
        return GeneticTest.objects.filter(species=species)

class GeneticTestStatistics(generics.GenericAPIView):
    def get(self, request, *args, **kwargs):
        from django.db.models import Avg, Max, Count
        stats = GeneticTest.objects.values('species').annotate(
            total_tests=Count('id'),
            avg_milk_yield=Avg('milk_yield'),
            max_milk_yield=Max('milk_yield'),
            good_health_percentage=Count('id', filter=models.Q(health_status='good')) * 100.0 / Count('id')
        )
        return Response({'statistics': stats})
