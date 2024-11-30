from django.urls import path
from .views import PostListView , postDetailsView
import pickle as pk

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'), 
    path('post/<int:pk>/', postDetailsView.as_view(), name='post-detail'),

]