from django.contrib import admin
from django.urls import path
from .views import registerUser ,LoginUser ,allUser

urlpatterns = [
     path('register',registerUser.as_view(),name='registerUser'),
     path('login',LoginUser.as_view(),name='LoginUser'),
       path('allUser',allUser.as_view(),name='allUser')
]
