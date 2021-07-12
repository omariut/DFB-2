from django.urls import path
from .views import BlogDeleteView, BlogDetailView, BlogListView, BlogCreateView, BlogUpdateView

urlpatterns = [
path('post/<int:pk>/edit/', BlogUpdateView.as_view(), name='post_edit'), # new
path('post/new/', BlogCreateView.as_view(), name='new-post'),

path('post/<int:pk>/', BlogDetailView.as_view(), name='post-detail'),
path('post/<int:pk>/delete/', BlogDeleteView.as_view(), name='post-delete'),
path('', BlogListView.as_view(), name='home'),
]
