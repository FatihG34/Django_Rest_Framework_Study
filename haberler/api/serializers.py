from rest_framework import serializers
from haberler.models import Makele

from datetime import datetime, date
from django.utils.timesince import timesince


class MakeleSerializer(serializers.ModelSerializer):
    time_since_pub = serializers.SerializerMethodField()
    class Meta:
        model=Makele
        fields = '__all__'
        # fields = ["author", "title", "content"]
        # exclude = ["created_time", "updated_date"]
        read_only_fields = ["id", "created_time", "updated_date"]
    
    def get_time_since_pub(self, obj):
        now = datetime.now()
        pub_time = obj.published_date
        if obj.is_active:
            time_delta = timesince(pub_time, now)
            return time_delta
        else:
            return 'This field can not be full, because; this Makele passive'
    
    def validate_published_date(self, pub_date):
        today = date.today()
        if pub_date > today:
            raise serializers.ValidationError('Published date can not be greater than today !')
        return pub_date


# Standart Serializer Code 👇🏻
class MakeleDefaultSerializer(serializers.Serializer):
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
    
    def validate(self, data):
        if data['title'] == data['description']:
            raise serializers.ValidationError('Title and Description must be different')
        return data

    def validate_title(self, value):
        if len(value) < 20 :
            raise serializers.ValidationError(f'Title must be greater than 20 char, you entered {len(value)}')
        return value