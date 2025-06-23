from django.urls import path
from about.views import AboutPageAPIView

urlpatterns = [
    path('page/', AboutPageAPIView.as_view(), name='about'),
]