from django.urls import path,include
from .import views
from .import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base', views.BASE, name='base'),
    path('home', views.HOME, name='home'),
    path('about',views.ABOUT,name='about'),
]
