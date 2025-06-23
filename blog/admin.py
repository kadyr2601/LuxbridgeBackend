from django.contrib import admin
from blog import models


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('slug',)

@admin.register(models.Blog)
class BlogAdmin(admin.ModelAdmin):
    readonly_fields = ('slug',)


@admin.register(models.Tag)
class TagAdmin(admin.ModelAdmin):
    readonly_fields = ('slug',)


admin.site.register(models.PopularTags)