import django_filters
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import filters
from django.db.models import Min, Max
from django_filters.rest_framework import DjangoFilterBackend
from projects.pagination import CustomPageNumberPagination
from projects.serializers import ProjectSerializer, SimilarProjectsSerializer, ProjectListSerializer
from projects.models import Project, SimilarProjects


class SimilarProjectsListAPIView(APIView):
    def get(self, request):
        obj = SimilarProjects.objects.first()
        serializer = SimilarProjectsSerializer(obj)
        return Response(serializer.data)


class ProjectFilter(django_filters.FilterSet):
    priceMin = django_filters.NumberFilter(field_name='starting_price', lookup_expr='gte')
    priceMax = django_filters.NumberFilter(field_name='starting_price', lookup_expr='lte')

    class Meta:
        model = Project
        fields = {
            'developer': ['exact'],          # Allows ?developer=Emaar
            'city': ['exact'],              # Allows ?city=Apartment
            'location': ['exact', 'icontains'],  # Allows ?location=Dubai or ?location__icontains=Palm
            'handover': ['exact'],          # Allows ?handover=3
        }


class ProjectsListView(ListAPIView):
    queryset = Project.objects.only('id', 'slug', 'name', 'featured', 'location', 'card_overview',
                                    'developer', 'starting_price', 'card_property_type', 'handover', 'card_image')
    serializer_class = ProjectListSerializer
    pagination_class = CustomPageNumberPagination

    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]

    filterset_class = ProjectFilter  # Use the custom FilterSet

    ordering_fields = ['starting_price', 'featured', 'handover']
    ordering = ['-featured']


class ProjectFiltersView(APIView):
    def get(self, request):
        developers = Project.objects.values('developer').distinct()
        cities = Project.objects.values('city').distinct()
        locations = Project.objects.values('location').distinct()
        handovers = Project.objects.values('handover').distinct()
        price_stats = Project.objects.aggregate(priceMin=Min('starting_price'), priceMax=Max('starting_price'))

        return Response({
            "developers": developers,
            "cities": cities,
            "locations": locations,
            "handovers": handovers,
            "priceMin": price_stats['priceMin'],
            "priceMax": price_stats['priceMax']
        })


class ProjectRetrieve(APIView):
    def get(self, request, slug):
        project = Project.objects.get(slug=slug)
        serializer = ProjectSerializer(project)
        return Response(serializer.data)