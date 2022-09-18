from rest_framework import serializers
from .models import Scrape

class ScrapeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scrape
        fields = '__all__'