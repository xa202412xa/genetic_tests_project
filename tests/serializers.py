from rest_framework import serializers
from .models import GeneticTest


class GeneticTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeneticTest
        fields = '__all__'

    def validate_health_status(self, value):
        if value not in ['good', 'poor']:
            raise serializers.ValidationError("Health status must be 'good' or 'poor'")
        return value