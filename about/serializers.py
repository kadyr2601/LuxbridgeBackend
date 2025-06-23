from rest_framework import serializers
from about.models import AboutPage


class AboutPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutPage
        fields = "__all__"
        depth = 1