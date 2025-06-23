from careers.models import MainBanner, Position, Application
from rest_framework import serializers


class MainBannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainBanner
        fields = '__all__'


class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = '__all__'


class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = '__all__'