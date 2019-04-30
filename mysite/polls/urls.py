from django.urls import path
from polls import views

urlpatterns = [
    path('index/', views.index, name="index"),
    path('form/', views.FormShow, name='form'),
    path('main/', views.MainPage, name='main'),
    path('', views.logouting, name='logout'),
]
