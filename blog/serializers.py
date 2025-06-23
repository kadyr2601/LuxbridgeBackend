from blog import models
from rest_framework import serializers
from blog.models import Blog


class CategorySerializer(serializers.ModelSerializer):
    count = serializers.SerializerMethodField()

    class Meta:
        model = models.Category
        fields = "__all__"

    def get_count(self, obj):
        return Blog.objects.filter(category=obj).count()


class PopularTagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PopularTags
        fields = "__all__"
        depth = 1


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Blog
        fields = "__all__"
        depth = 1