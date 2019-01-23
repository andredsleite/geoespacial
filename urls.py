from django.urls import path
from .views import panda
urlpatterns = [
    path('', panda),
]
