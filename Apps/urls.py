from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', AppStockValuation, name='AppStockValuation'),    
]