from rest_framework import serializers


class ErrorResponseSerializer(serializers.Serializer):
    status_code = serializers.IntegerField()
    errors = serializers.CharField()


class EmptySerializer(serializers.Serializer):
    pass
