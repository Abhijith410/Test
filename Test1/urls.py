from django.urls import path
from . import views

urlpatterns = [
    path('test/', views.fun1, name="Iphone")
]