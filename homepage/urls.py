from django.urls import path
from homepage import views
from homepage.views import PropertyTypesView

urlpatterns = [
    path('retrieve/', views.HomePageView.as_view(), name='retrieve'),
    path('property-types/', PropertyTypesView.as_view(), name='property-types'),
]