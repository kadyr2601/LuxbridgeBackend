from django.urls import path
from other.views import SeoRetrieve, ClientFeedbackCreate


urlpatterns = [
    path('seo/<slug>/', SeoRetrieve.as_view()),
    path('feedback-create/', ClientFeedbackCreate.as_view()),
]