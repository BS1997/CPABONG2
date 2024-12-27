from django.urls import path
from . import views
from .views import about_cpabong

urlpatterns = [
    path('', about_cpabong, name='about_cpabong'),    
]