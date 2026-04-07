from django.shortcuts import render

# Create your views here.
from .serializers import StreamPlatformSerialiser,WatchListSerialiser ,ReviewSerialiser
from .models import StreamPlatform, WatchList ,Review
from rest_framework.views import APIView
from rest_framework.response import  Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated

# class ReviewAV(APIView):
#     def get(self,request,pk):
#         rating=Review.objects.all(pk=pk)
#         serialiser=ReviewSerialiser(many=True,pk=request.pk)
#         return Response (serialiser.data,
#                              status=status.HTTP_200_OK)

# created a view using mixins and generic view

from rest_framework import mixins
from rest_framework import generics

class ReviewDetails(generics.GenericAPIView, mixins.ListModelMixin):
    queryset = Review.objects.all()
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
class ReviewList( mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Review.objects.all()
    serializer_class=ReviewSerialiser

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    

class WatchListAV(APIView):

    def get(self,request):
        watch=WatchList.objects.all()
        serialiser=WatchListSerialiser(watch,many=True)
        return Response (serialiser.data,
                             status=status.HTTP_200_OK)
         
        
    def post(self,request):
        serializer=WatchListSerialiser(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response  (
                             status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST

            )
        

class StreamPlatformAV(APIView):
    def get(self,request):
        SPl=StreamPlatform.objects.all()
        serialiser=StreamPlatformSerialiser(SPl ,many=True)
        return Response(serialiser.data)
    
    def get(self,request,pk):
        SPl=StreamPlatform.objects.filter(pk=pk)
        serialiser=StreamPlatformSerialiser(SPl, many=True)
        return Response(serialiser.data)

    def post(self,request):
        serializer=StreamPlatformSerialiser(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data,
                             status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST

            )

# class LoginUser(APIView):
#     def post(self,request):
#         data=request.data

#         username=data.get('username')
#         password=data.get('password')

#         user=User.objects.filter(username=username).first()
#         if user and user.check_password(password):
#              refresh=RefreshToken.for_user(user)

#              return Response(   {
#                  "access_token": str(refresh.access_token),
#                  "refresh_token": str(refresh),
#                   "message ":"login Successfully "
#              }
#                  )
#         return Response({"message ":  "invailid creadentials try again"},status=status.HTTP_400_BAD_REQUEST )
    

# class UserProfile(APIView):
#     permission_classes =[IsAuthenticated]
#     def get(self,request):
#         user =request.user
#         serailizer=UserSerializer(user)
#         return Response(serailizer.data  )
        


