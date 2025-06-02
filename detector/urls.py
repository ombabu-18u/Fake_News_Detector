from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('submit/', views.submit_news, name='submit'),
    path('results/', views.results, name='results'),
]