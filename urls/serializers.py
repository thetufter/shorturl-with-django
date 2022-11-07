from rest_framework import serializers
from .models import URL


class URLSerializer(serializers.ModelSerializer):
    class Meta:
        model = URL
        fields = ["key", "secret_key", "target_url", "clicks"]
