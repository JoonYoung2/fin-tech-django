from django.contrib import admin
from django.urls import path
from spring_test import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/', views.test),
    path('bank/', views.bank),
]
