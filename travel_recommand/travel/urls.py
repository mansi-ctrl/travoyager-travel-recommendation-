from django.conf.urls import url
from django.urls import path
from .views import *
import datetime

urlpatterns = [
    path('', index, name='index'),

    path('userRegister', userRegister, name='userRegister'),
    path('userLogin', userLogin, name='userLogin'),

    path('userInput', userInput, name='userInput'),
    path('split_userInput', split_userInput, name='split_userInput'),

    path('placeFetch', placeFetch, name='placeFetch'),
    path('temp', temp, name='temp'),
    path('tempDelete/<int:pk>', tempDelete, name='tempDelete'),
    path('addPlace/<int:counter>', addPlace, name='addPlace'),
    path('addPlace/addPlaceEntry/<int:pk>/<int:location>', addPlaceEntry, name='addPlaceEntry'),
    path('updatePlace/<int:pk>/<int:counter>', updatePlace, name='updatePlace'),

]