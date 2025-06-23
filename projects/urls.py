from django.urls import path
from projects import views
from projects.views import SimilarProjectsListAPIView

urlpatterns = [
    path('filters/', views.ProjectFiltersView.as_view()),
    path('list/', views.ProjectsListView.as_view()),
    path('retrieve/<slug>/', views.ProjectRetrieve.as_view()),
    path('similar/', SimilarProjectsListAPIView.as_view()),
]