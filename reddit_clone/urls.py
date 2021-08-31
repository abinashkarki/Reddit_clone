from django.contrib import admin
from django.urls import path, include
from . import views 
from .views import SubredditList
urlpatterns = [
    path('posts/',views.SubredditList.as_view()),
    path('posts/<int:pk>/', views.SubredditDetailView.as_view()),
    path('posts/<int:pk>/vote', views.VoteCreate.as_view()),
    path('posts/votes', views.VoteAPIListView.as_view()),
    path('posts/votes/<int:pk>/', views.VoteAPIDetailListView.as_view()),
    path('posts/votes/<int:pk>/delete', views.VoteAPIDeleteView.as_view()),
]