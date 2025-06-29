from rest_framework import views, response, generics
from other import serializers, models


class SeoRetrieve(views.APIView):
    def get(self, request, slug):
        seo = models.Seo.objects.get(page=slug)
        serializer = serializers.SeoSerializer(seo)
        return response.Response(serializer.data)


class ClientFeedbackCreate(generics.CreateAPIView):
    serializer_class = serializers.ClientFeedbackSerializer