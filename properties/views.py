from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from properties.models import Property, AdditionalProperties
from properties.pagination import CustomPageNumberPagination
from properties.serializers import PropertySerializer, PropertyListSerializer, AdditionalPropertiesSerializer


class PropertyListView(ListAPIView):
    queryset = Property.objects.only(
        'id', 'ref', 'card_image', 'price', 'name', 'overview', 'bedrooms', 'bathrooms', 'area', 'status', 'location')
    serializer_class = PropertyListSerializer
    pagination_class = CustomPageNumberPagination

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]

    search_fields = ['location', 'name', 'ref']
    # Example: /api/properties/?search=palm

    filterset_fields = {
        'for_rent': ['exact'], # Allows ?for_rent=true or ?for_rent=false
        'type': ['exact'],     # Allows ?type=Apartment
        'bedrooms': ['exact',], # Allows ?bedrooms=3
        'bathrooms': ['exact',], # Allows ?bathrooms=2
        'location': ['exact', 'icontains'], # Allows ?location=Dubai or ?location__icontains=Palm
        'status': ['exact'], # Allows ?status=Ready
    }
    # Example: /api/properties/?for_rent=false&type=Villa&bedrooms=3

    ordering_fields = ['price', 'id']
    ordering = ['-id']
    # Example: /api/properties/?ordering=price (low to high)
    # Example: /api/properties/?ordering=-price (high to low)


class PropertyFiltersView(APIView):
    def get(self, request):
        property_types = Property.objects.values('type').distinct()
        property_locations = Property.objects.values('location').distinct()
        property_statuses = Property.objects.values('status').distinct()
        property_bedrooms = Property.objects.values('bedrooms').distinct()
        property_bathrooms = Property.objects.values('bathrooms').distinct()
        return Response({"property_types": property_types, "property_locations": property_locations,
                         "property_statuses": property_statuses, "property_bedrooms": property_bedrooms,
                         "property_bathrooms": property_bathrooms})


class PropertyRetrieve(APIView):
    def get(self, request, slug):
        property = Property.objects.get(ref=slug)
        serializer = PropertySerializer(property)
        return Response(serializer.data)


class SimilarPropertiesView(APIView):
    def get(self, request, slug):
        obj = AdditionalProperties.objects.get(page=slug)
        serializer = AdditionalPropertiesSerializer(obj)
        return Response(serializer.data)