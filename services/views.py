from services import models, serializers
from rest_framework import views
from rest_framework.response import Response


class ServicesPageView(views.APIView):
    def get(self, request):
        banner = models.MainBanner.objects.first()
        services = models.Service.objects.all()
        faqs = models.FAQs.objects.all()

        banner_serializer = serializers.MainBannerSerializer(banner)
        services_serializer = serializers.ServiceSerializer(services, many=True)
        faqs_serializer = serializers.FAQsSerializer(faqs, many=True)
        data = {
            "banner": banner_serializer.data,
            "services": services_serializer.data,
            "faqs": faqs_serializer.data,
        }
        return Response(data)


class ServicesRetrieve(views.APIView):
    def get(self, request, slug):
        services = models.Service.objects.get(slug=slug)
        serializer = serializers.ServiceSerializer(services)
        return Response(serializer.data)


