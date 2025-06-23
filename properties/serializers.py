from rest_framework import serializers
from properties.models import Property, PropertyGallery, NearbyPlace, AdditionalProperties


class AdditionalPropertiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdditionalProperties
        fields = '__all__'
        depth = 1


class PropertyGallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyGallery
        fields = '__all__'


class NearbyPlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = NearbyPlace
        fields = '__all__'


class PropertySerializer(serializers.ModelSerializer):
    gallery = PropertyGallerySerializer(many=True)
    nearby_places = NearbyPlaceSerializer(many=True)

    class Meta:
        model = Property
        fields = '__all__'


class PropertyListSerializer(serializers.ModelSerializer):
    card_image = serializers.SerializerMethodField()

    class Meta:
        model = Property
        fields = ['id', 'ref', 'status', 'card_image', 'price', 'location', 'name', 'overview', 'bedrooms', 'bathrooms', 'area']

    def get_card_image(self, obj):
        if obj.card_image:
            return obj.card_image.url
        return None