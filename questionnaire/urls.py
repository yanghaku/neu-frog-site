from django.urls import path
from questionnaire import views

urlpatterns = [
    path('', views.question, name='question'),
]