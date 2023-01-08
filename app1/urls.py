from django.urls import path
from app1.views import *

app_name='something'

urlpatterns = [
    path('app_1/',app_1,name='app_1'),
]
