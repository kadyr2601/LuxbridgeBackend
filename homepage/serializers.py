from rest_framework import serializers
from homepage.models import (MainBanner, FeaturedPropertiesBanner, PartnersBanner, FeaturedProjectsBanner,
                             ServicesBanner, ProjectsByCityBanner, OurExperienceBanner, TestimonialsBanner)


class MainBannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainBanner
        fields = '__all__'


class FeaturedPropertiesBannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeaturedPropertiesBanner
        fields = '__all__'
        depth = 1


class PartnersBannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartnersBanner
        fields = '__all__'


class FeaturedProjectsBannerSerializer(serializers.ModelSerializer):
    project_slug = serializers.SerializerMethodField()

    class Meta:
        model = FeaturedProjectsBanner
        fields = '__all__'

    def get_project_slug(self, obj):
        return obj.project.slug


class ServicesBannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServicesBanner
        fields = '__all__'
        depth = 1


class ProjectsByCityBannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectsByCityBanner
        fields = '__all__'


class OurExperienceBannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = OurExperienceBanner
        fields = '__all__'


class TestimonialsBannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestimonialsBanner
        fields = '__all__'