from django.urls import path
from blog.views import CategoryListView, PopularTagsListView, BlogListView, BlogDetailView, CategoryRetrieveView, TagRetrieveView

urlpatterns = [
    path('categories/', CategoryListView.as_view()),
    path('category/<slug>/', CategoryRetrieveView.as_view()),
    path('tag/<slug>/', TagRetrieveView.as_view()),
    path('tags/', PopularTagsListView.as_view()),
    path('list/', BlogListView.as_view()),
    path('retrieve/<slug>/', BlogDetailView.as_view()),
]
