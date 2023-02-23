from django.urls import path
from .views import *

urlpatterns = [
    path('BB/', BB.as_view(), name='BB'),
    ]