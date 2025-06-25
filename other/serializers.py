from rest_framework import serializers
from other import models


class SeoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Seo
        fields = '__all__'


class ClientFeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ClientFeedback
        fields = '__all__'