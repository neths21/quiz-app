from django.urls import path
from quiz import views

urlpatterns = [
    path('question/', views.question, name='question'),
    path('results/', views.results, name='results'),
]