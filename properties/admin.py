from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from properties.models import Property, PropertyGallery, NearbyPlace, AdditionalProperties


admin.site.register(AdditionalProperties)


class PropertyGalleryInline(admin.TabularInline):
    model = PropertyGallery
    extra = 0


class PropertyNearbyInline(admin.StackedInline):
    model = NearbyPlace
    extra = 0


class PropertyResource(resources.ModelResource):
    class Meta:
        model = Property
        fields = ('id', 'ref', 'name', 'location', 'price', 'bedrooms', 'bathrooms', 'area', 'overview', 'features',
                  'amenities', 'map', 'type', 'status', 'for_rent')
        export_order = fields
        skip_unchanged = True
        report_skipped = True
        exclude = ('card_image',)

    def before_import_row(self, row, **kwargs):
        # Clean price
        if 'price' in row and row['price']:
            price_raw = str(row['price']).replace(',', '').replace('.', '')
            row['price'] = int(price_raw)

        # Clean area if it’s also decimal
        if 'area' in row and row['area']:
            area_raw = str(row['area']).replace(',', '').replace('.', '')
            row['area'] = int(area_raw)


@admin.register(Property)
class PropertyAdmin(ImportExportModelAdmin):
    resource_class = PropertyResource
    inlines = [PropertyGalleryInline, PropertyNearbyInline]
    list_display = ('name', 'type', 'location')
    list_filter = ('type',)