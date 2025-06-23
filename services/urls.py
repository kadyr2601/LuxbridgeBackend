from django.urls import path
from services import views

urlpatterns = [
    path('page/', views.ServicesPageView.as_view()),
    path('details/<slug>/', views.ServicesRetrieve.as_view(), name='service-details'),
]