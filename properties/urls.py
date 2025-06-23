from django.urls import path
from properties.views import PropertyListView, PropertyFiltersView, PropertyRetrieve, SimilarPropertiesView

urlpatterns = [
    path('list/', PropertyListView.as_view()),
    path('filters/', PropertyFiltersView.as_view()),
    path('retrieve/<slug>/', PropertyRetrieve.as_view()),
    path('similar/<slug>/', SimilarPropertiesView.as_view()),
]
