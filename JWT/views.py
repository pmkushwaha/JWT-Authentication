from django.shortcuts import render

# Create your views here.
from .serializers import UserSerializer
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import  Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated

class registerUser(APIView):

    def post(self,request):
        serializer=UserSerializer(data=request.data)
        if serializer.is_valid():
            user=serializer.save()
            return Response (serializer.data,
                             status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST

            )
        

class allUser(APIView):
    def get(self,request):
        users=User.objects.all()
        serialiser=UserSerializer(users ,many=True)
        return Response(serialiser.data)

class LoginUser(APIView):
    def post(self,request):
        data=request.data

        username=data.get('username')
        password=data.get('password')

        user=User.objects.filter(username=username).first()
        if user and user.check_password(password):
             refresh=RefreshToken.for_user(user)

             return Response(   {
                 "access_token": str(refresh.access_token),
                 "refresh_token": str(refresh),
                  "message ":"login Successfully "
             }
                 )
        return Response({"message ":  "invailid creadentials try again"},status=status.HTTP_400_BAD_REQUEST )
    

class UserProfile(APIView):
    permission_classes =[IsAuthenticated]
    def get(self,request):
        user =request.user
        serailizer=UserSerializer(user)
        return Response(serailizer.data  )
        


