"""the serializers
"""
from rest_framework import serializers


class SingleArticleSerializer(serializers.Serializer):
    title = serializers.CharField(
        required=True,
        allow_null=False, allow_blank=False,
        max_length=128)
    cover = serializers.CharField(
        required=True,
        allow_null=False, allow_blank=False,
        max_length=256)
    content = serializers.CharField(
        required=True,
        allow_null=False, allow_blank=False,
        max_length=2048)
    created_at = serializers.DateTimeField(
        required=True,
        allow_null=False)
