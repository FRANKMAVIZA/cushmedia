from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contactform', views.contactform, name='contactform')
]