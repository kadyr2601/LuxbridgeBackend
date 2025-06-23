from django.contrib import admin
from homepage.models import (MainBanner, FeaturedPropertiesBanner, PartnersBanner, FeaturedProjectsBanner,
                             ServicesBanner, ProjectsByCityBanner, OurExperienceBanner, TestimonialsBanner)


admin.site.register(MainBanner)
admin.site.register(FeaturedPropertiesBanner)
admin.site.register(PartnersBanner)
admin.site.register(FeaturedProjectsBanner)
admin.site.register(ServicesBanner)
admin.site.register(ProjectsByCityBanner)
admin.site.register(OurExperienceBanner)
admin.site.register(TestimonialsBanner)