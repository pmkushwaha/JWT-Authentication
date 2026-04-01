from django.contrib import admin
from django.urls import path
from .views import  StreamPlatformAV,WatchListAV
# from .views import registerUser ,LoginUser ,allUser,UserProfile
urlpatterns = [
     path('platform',StreamPlatformAV.as_view(),name='StreamPlatform'),
     path('watchlist',WatchListAV.as_view(),name='WatchList'),
      #  path('allUser',allUser.as_view(),name='allUser'),
      #  path('UserProfile',UserProfile.as_view(),name='UserProfile'),
]
