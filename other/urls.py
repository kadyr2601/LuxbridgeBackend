from django.urls import path
from other.views import SeoRetrieve


urlpatterns = [
    path('seo/<slug>/', SeoRetrieve.as_view()),
]