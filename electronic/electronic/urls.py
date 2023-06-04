from django.contrib import admin
from django.urls import path
from electronic_library import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main, name='main'),
    path('basket/', views.basket, name='basket'),
    path('stuff/', views.stuff, name='stuff'),
]
