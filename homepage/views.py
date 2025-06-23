from rest_framework.views import APIView
from rest_framework.response import Response
from homepage.models import (MainBanner, FeaturedPropertiesBanner, PartnersBanner, FeaturedProjectsBanner,
                             ProjectsByCityBanner, OurExperienceBanner, TestimonialsBanner, ServicesBanner)
from homepage.serializers import MainBannerSerializer, FeaturedPropertiesBannerSerializer, PartnersBannerSerializer, \
    FeaturedProjectsBannerSerializer, ProjectsByCityBannerSerializer, OurExperienceBannerSerializer, \
    TestimonialsBannerSerializer, ServicesBannerSerializer
from properties.models import Property


class HomePageView(APIView):
    def get(self, request):
        main_banner = MainBanner.objects.all()
        featured_properties = FeaturedPropertiesBanner.objects.first()
        partners_banner = PartnersBanner.objects.all()
        featured_projects = FeaturedProjectsBanner.objects.all()
        projects_by_city_banner = ProjectsByCityBanner.objects.all()
        our_experience_banner = OurExperienceBanner.objects.first()
        testimonials_banner = TestimonialsBanner.objects.all()
        property_types = Property.objects.values('type').distinct()
        services_banner = ServicesBanner.objects.first()

        main_banner_serializer = MainBannerSerializer(main_banner, many=True)
        featured_properties_serializer = FeaturedPropertiesBannerSerializer(featured_properties)
        partners_banner_serializer = PartnersBannerSerializer(partners_banner, many=True)
        featured_projects_serializer = FeaturedProjectsBannerSerializer(featured_projects, many=True)
        projects_by_city_banner_serializer = ProjectsByCityBannerSerializer(projects_by_city_banner, many=True)
        our_experience_banner_serializer = OurExperienceBannerSerializer(our_experience_banner)
        testimonials_banner_serializer = TestimonialsBannerSerializer(testimonials_banner, many=True)
        services_banner_serializer = ServicesBannerSerializer(services_banner)

        data = {
            "main_banner": main_banner_serializer.data,
            "featured_properties": featured_properties_serializer.data,
            "property_types": property_types,
            "partners_banner": partners_banner_serializer.data,
            "featured_projects": featured_projects_serializer.data,
            "projects_by_city_banner": projects_by_city_banner_serializer.data,
            "our_experience_banner": our_experience_banner_serializer.data,
            "testimonials_banner": testimonials_banner_serializer.data,
            "services_banner": services_banner_serializer.data,
        }
        return Response(data)


class PropertyTypesView(APIView):
    def get(self, request):
        property_types = Property.objects.values('type').distinct()
        return Response(property_types)