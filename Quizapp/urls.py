from django.urls import path
from Quizapp import views

urlpatterns = [
    path('home/', views.home, name='home')
]
