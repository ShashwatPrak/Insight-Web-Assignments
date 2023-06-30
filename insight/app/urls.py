from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name="home"),
    path('addarticle/', views.addarticle, name="add"),
    path('deletearticle/<str:pk>/', views.deletearticle, name="delete"),
    path('updatearticle/<str:pk>/', views.updatearticle, name="update")

]
