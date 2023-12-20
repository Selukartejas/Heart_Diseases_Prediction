
from django.urls import path, include
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('feedback/', views.feedback),
    path('homes/', views.homes, name='homes'),

    path('input/', views.input, name='input'),
    path('result/', views.result, name='result'),


]
