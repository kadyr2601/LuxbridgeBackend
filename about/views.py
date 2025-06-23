from rest_framework.response import Response
from about.serializers import AboutPageSerializer
from about.models import AboutPage
from rest_framework.views import APIView


class AboutPageAPIView(APIView):
    def get(self, request):
        page = AboutPage.objects.first()
        serializer = AboutPageSerializer(page)
        return Response(serializer.data)