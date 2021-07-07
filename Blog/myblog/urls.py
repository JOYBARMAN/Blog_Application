from django.urls import path
from . import views
from . views import HomeView,ArticaleDetailView,AddPostView,UpdatePostView,DeletePostView

urlpatterns = [
    path('',HomeView.as_view(),name="home"),
    path('articale/<int:pk>',ArticaleDetailView.as_view(),name="articale-detail"),
    path('add_post/',AddPostView.as_view(),name="add_post"),
    path('articale/edit/<int:pk>',UpdatePostView.as_view(),name="update_post"),
    path('articale/<int:pk>/remove',DeletePostView.as_view(),name="delete_post"),
]
