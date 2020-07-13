from django.contrib import admin
from django.urls import path
from myapp import views

app_name = 'myapp'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.base, name = 'base'),
    path('index/', views.index, name = 'index'),
    path('forms/', views.form, name = 'form'),
]
