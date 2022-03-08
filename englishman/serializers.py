from rest_framework import serializers

class EnglishSerializer(serializers.Serializer):
    text = serializers.CharField()

