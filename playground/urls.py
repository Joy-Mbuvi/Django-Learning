from django.urls import path
from . import views


urlpatterns=[
    path('hello/', views.say_hello),
    path('bee/' , views.big_back),
    path('create/',views.create,name='create'),


]