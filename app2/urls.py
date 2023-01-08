from django.urls import path
from app2.views import *

app_name="new"



urlpatterns = [
    path('app_2/',app_2,name='app_2'),
]
