from django.urls import path
from Quizapp import views

urlpatterns = [
    path('', views.home, name='home')
]
