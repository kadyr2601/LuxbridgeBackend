from rest_framework import serializers
from projects.models import (PropertyType, Project, ProjectGallery, NearbyPlace,
                             DownloadedInformation, SimilarProjects)


class PropertyTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyType
        fields = '__all__'


class ProjectGallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectGallery
        fields = '__all__'


class NearbyPlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = NearbyPlace
        fields = '__all__'


class DownloadedInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = DownloadedInformation
        fields = '__all__'


class SimilarProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SimilarProjects
        fields = '__all__'
        depth = 1


class ProjectSerializer(serializers.ModelSerializer):
    downloaded_informations = DownloadedInformationSerializer(many=True, read_only=True)
    nearby_places = NearbyPlaceSerializer(many=True, read_only=True)
    project_gallery = ProjectGallerySerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = '__all__'
        depth = 1


class ProjectListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'slug', 'name', 'featured', 'location', 'card_overview', 'developer', 'starting_price',
                  'card_property_type', 'handover', 'card_image']