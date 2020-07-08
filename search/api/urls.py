from rest_framework import routers
from . import views
from django.urls import path


router = routers.DefaultRouter()

urlpatterns = [
    path('search/', views.SearchListView.as_view()),
]
