from django.urls import path
from .views import GeneticTestListCreate, GeneticTestListBySpecies, GeneticTestStatistics

urlpatterns = [
    path('tests', GeneticTestListCreate.as_view(), name='test-list-create'),
    path('tests/species', GeneticTestListBySpecies.as_view(), name='test-list-by-species'),
    path('statistics', GeneticTestStatistics.as_view(), name='test-statistics'),
]

