from django.urls import path
from . import views

urlpatterns = [
    path('helloworld/', views.helloWorld),
    path("", views.tasksList),
    path('yourname/<str:name>',views.yourName,name = 'your-name')
]
