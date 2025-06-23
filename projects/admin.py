from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from projects.models import (PropertyType, Project, ProjectGallery, NearbyPlace,
                             DownloadedInformation, SimilarProjects)


admin.site.register(PropertyType)
admin.site.register(SimilarProjects)


class ProjectGalleryInline(admin.StackedInline):
    model = ProjectGallery
    extra = 0


class NearbyPlaceInline(admin.StackedInline):
    model = NearbyPlace
    extra = 0


class DownloadedInformationInline(admin.StackedInline):
    model = DownloadedInformation
    extra = 0


class ProjectResource(resources.ModelResource):
    class Meta:
        model = Project
        fields = ('id', 'name', 'slug', 'location', 'card_overview', 'developer', 'city', 'card_property_type',
                  'starting_price', 'handover', 'status', 'amenities', 'map_location', 'featured')
        export_order = fields
        skip_unchanged = True
        report_skipped = True
        exclude = ('card_image', 'mainBanner', 'property_types')

    def before_import_row(self, row, **kwargs):
        # Clean price
        if 'price' in row and row['price']:
            price_raw = str(row['price']).replace(',', '').replace('.', '')
            row['price'] = int(price_raw)



@admin.register(Project)
class ProjectAdmin(ImportExportModelAdmin):
    resource_class = ProjectResource
    inlines = [NearbyPlaceInline, DownloadedInformationInline, ProjectGalleryInline]
    readonly_fields = ('slug',)