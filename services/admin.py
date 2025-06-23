from django.contrib import admin
from services.models import MainBanner, FAQs, Service, ServiceStep

admin.site.register(MainBanner)
admin.site.register(FAQs)


class ServiceStepInline(admin.StackedInline):
    model = ServiceStep
    extra = 0


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    inlines = [ServiceStepInline,]
    readonly_fields = ('slug',)