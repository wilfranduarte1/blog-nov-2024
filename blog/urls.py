from django.urls import path
from .views import PostListView , postDetailsView, PostCreateView
import pickle as pk
from.views import PostUpdateView
from.views import PostDeleteView

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'), 
    path('post/<int:pk>/', postDetailsView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-new'), 
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    ]