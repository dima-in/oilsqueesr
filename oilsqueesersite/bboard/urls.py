from django.urls import path

from .views import index
"""
urlpatterns список маршрутов уровня приложения
"""

urlpatterns = [
    path('', index),
]