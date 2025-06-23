from rest_framework.response import Response
from careers import models, serializers
from rest_framework import generics, views


class PositionView(generics.ListAPIView):
    queryset = models.Position.objects.all()
    serializer_class = serializers.PositionSerializer


class ApplicationCreateView(generics.CreateAPIView):
    serializer_class = serializers.ApplicationSerializer


class MainBannerView(views.APIView):
    def get(self, request):
        banner = models.MainBanner.objects.first()
        serializer = serializers.MainBannerSerializer(banner)
        return Response(serializer.data)