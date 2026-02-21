from django.contrib import admin
from django.urls import path
from .views import registerUser ,LoginUser ,allUser,UserProfile

urlpatterns = [
     path('register',registerUser.as_view(),name='registerUser'),
     path('login',LoginUser.as_view(),name='LoginUser'),
       path('allUser',allUser.as_view(),name='allUser'),
       path('UserProfile',UserProfile.as_view(),name='UserProfile'),
]
