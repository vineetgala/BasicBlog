from django.urls import path
from . import views
from .views import PostListView, PostDeleteView
from .views import PostCreateView, PostUpdateView

urlpatterns = [
	path('posts/<int:pk>/update',PostUpdateView.as_view(), name="post-update"),
	path('posts/<int:pk>/delete',PostDeleteView.as_view(), name="post-delete"),
	path('posts/new/',PostCreateView.as_view(), name="post-create"),
	path('',PostListView.as_view(), name="blog-home"),	
    path('about/',views.about, name="blog-about"),
]