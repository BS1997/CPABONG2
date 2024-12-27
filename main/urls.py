from django.urls import path
from . import views
from .views import cpabong_main

urlpatterns = [
    path('', cpabong_main, name='cpabong_main'),    
]