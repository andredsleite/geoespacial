from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('produtos.url')),
    path('admin/', admin.site.urls),
    path('pandas', include('pandas.urls')),
]
