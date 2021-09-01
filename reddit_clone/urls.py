from django.contrib import admin
from django.urls import path, include
from . import views 
from .views import SubredditList
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('posts/',views.SubredditList.as_view()),
    path('posts/<int:pk>/', views.SubredditDetailView.as_view()),
    path('posts/<int:pk>/vote', views.VoteCreate.as_view()),
    path('posts/votes', views.VoteAPIListView.as_view()),
    path('posts/votes/<int:pk>/', views.VoteAPIDetailListView.as_view()),
    path('posts/votes/<int:pk>/delete', views.VoteAPIDeleteView.as_view()),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]