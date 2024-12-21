from django.urls import path
from .views import (HomePageView, AboutPageView, BlogListView,
                    BlogDetailView, BlogCreateView, BlogUpdateView,
                    BlogDeleteView)

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
]
