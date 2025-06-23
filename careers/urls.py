from django.urls import path
from careers import views

urlpatterns = [
    path('banner/', views.MainBannerView.as_view(), name='main-banner'),
    path('positions/', views.PositionView.as_view(), name='positions'),
    path('apply/', views.ApplicationCreateView.as_view(), name='application-create'),
]
