from rest_framework import views
from rest_framework.response import Response
from blog import serializers, models


class CategoryListView(views.APIView):
    def get(self, request):
        categories = models.Category.objects.all()
        serializer = serializers.CategorySerializer(categories, many=True)
        return Response(serializer.data)


class PopularTagsListView(views.APIView):
    def get(self, request):
        tags = models.PopularTags.objects.first()
        serializer = serializers.PopularTagsSerializer(tags)
        return Response(serializer.data)


class BlogListView(views.APIView):
    def get(self, request):
        blogs = models.Blog.objects.all()
        serializer = serializers.BlogSerializer(blogs, many=True)
        return Response(serializer.data)


class BlogDetailView(views.APIView):
    def get(self, request, slug):
        blog = models.Blog.objects.get(slug=slug)
        serializer = serializers.BlogSerializer(blog)
        return Response(serializer.data)


class CategoryRetrieveView(views.APIView):
    def get(self, request, slug):
        posts = models.Blog.objects.filter(category__slug=slug)
        serializer = serializers.BlogSerializer(posts, many=True)
        return Response(serializer.data)


class TagRetrieveView(views.APIView):
    def get(self, request, slug):
        posts = models.Blog.objects.filter(tags__slug=slug)
        serializer = serializers.BlogSerializer(posts, many=True)
        return Response(serializer.data)