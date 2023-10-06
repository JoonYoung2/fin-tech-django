from django.contrib import admin
from django.urls import path

from drf_test import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/', views.test),
    path('ajax/', views.ajax),
    path('result/', views.result),
]
