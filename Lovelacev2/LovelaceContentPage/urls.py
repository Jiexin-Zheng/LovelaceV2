from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
	path('example1.html', views.example1view, name='example1view'),
	path('example2.html', views.example2view, name='example2view'),
]
