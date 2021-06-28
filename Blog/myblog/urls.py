from django.urls import path
from . import views
from . views import HomeView,ArticaleDetailView

urlpatterns = [
    path('',HomeView.as_view(),name="home"),
    path('articale/<int:pk>',ArticaleDetailView.as_view(),name="articale-detail"),
]
