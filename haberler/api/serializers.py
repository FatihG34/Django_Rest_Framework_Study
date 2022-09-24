from rest_framework import serializers
from haberler.models import Makele


class MakeleSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    author = serializers.CharField()
    title = serializers.CharField()
    description = serializers.CharField()
    content = serializers.CharField()
    country = serializers.CharField()
    published_date = serializers.DateField()
    is_active = serializers.BooleanField()
    created_time = serializers.DateTimeField(read_only=True)
    updated_date = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        print(validated_data)
        return Makele.objects.create(**validated_data)


    def update(self, instance, validated_data):
        instance.author = validated_data.get("author", instance.author)
        instance.title = validated_data.get("title", instance.title)
        instance.description = validated_data.get("description", instance.description)
        instance.content = validated_data.get("content", instance.content)
        instance.country = validated_data.get("country", instance.country)
        instance.published_date = validated_data.get("published_date", instance.published_date)
        instance.is_active = validated_data.get("is_active", instance.is_active)
        instance.save()
        return instance