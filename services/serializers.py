from services.models import MainBanner, FAQs, Service, ServiceStep
from rest_framework import serializers


class FAQsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQs
        fields = '__all__'


class MainBannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainBanner
        fields = '__all__'


class ServiceStepsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceStep
        fields = '__all__'


class ServiceSerializer(serializers.ModelSerializer):
    processSteps = ServiceStepsSerializer(many=True, read_only=True)
    class Meta:
        model = Service
        fields = '__all__'