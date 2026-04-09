from django.contrib import admin
from django.urls import path
from .views import  StreamPlatformAV,WatchListAV ,ReviewList,ReviewDetails,WatchDetails ,CreateReview
# from .views import registerUser ,LoginUser ,allUser,UserProfile
urlpatterns = [
     path('platform',StreamPlatformAV.as_view(),name='StreamPlatform'),
     path('platform/<int:pk>',StreamPlatformAV.as_view(),name='StreamPlatform_Details'),
     path('watchlist',WatchListAV.as_view(),name='WatchList'),
     path('watchDetails/<int:pk>',WatchDetails.as_view(),name='WatchList_Detail'),


     path("watchlist/<int:pk>/Review-Create",CreateReview.as_view(), name="CreateReview"),
     path("watchlist/<int:pk>/Review",ReviewList.as_view(), name="Review_list"),
     path("watchlist/ReviewDetails/<int:pk>",ReviewDetails.as_view(), name="ReviewDetails")

      #  path('allUser',allUser.as_view(),name='allUser'),
      #  path('UserProfile',UserProfile.as_view(),name='UserProfile'),
]
