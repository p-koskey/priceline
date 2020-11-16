from django.shortcuts import render
from django.http  import HttpResponse
from .serializers import UserSerializer, ProfileSerializer
from .models import Profile
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.contrib.auth import get_user_model
User = get_user_model()
from .permissions import IsCompanyAdmin, IsNormalUser,IsVendor, UserIsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class UserView(APIView):
    permission_classes = (IsAuthenticated,IsCompanyAdmin)
    def get(self,request):
        try:
            users = User.objects.all()
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        if request.method == 'GET':
            serializer = UserSerializer(users, many=True)
            return Response(serializer.data)

class ProfileView(APIView):
    permission_classes = (IsAuthenticated,)
    def post(self,request,id):
        user = request.user
        try:
            user_profile = User.objects.get(id=id)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        if user_profile != user:
            return Response({'response': "You don't have permission to edit that"})
        if request.method == 'POST':
            
            serializer = ProfileSerializer(data=request.data,context={'request':request})
            data = {}
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class ProfilesView(APIView):
    permission_classes = (IsAuthenticated,IsCompanyAdmin)
    def get(self,request):
        try:
            profiles= Profile.objects.all()
        except Profile.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        if request.method == 'GET':
            serializer = ProfileSerializer(profiles, many=True)
            return Response(serializer.data)

class ProfileIdView(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self,request):
        user = request.user
        try:
            profile= Profile.objects.get(user=user)
        except Profile.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        if request.method == 'GET':
            serializer = ProfileSerializer(profile,context={'request':request})
            return Response(serializer.data)

class UpdateProfileView(APIView):
    permission_classes = (IsAuthenticated,)
    def put(self,request):
        user = request.user
        try:
            profile= Profile.objects.get(user=user)
        except Profile.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        if request.method == 'PUT':
            serializer = ProfileSerializer(profile,data=request.data,context={'request':request})
            data = {}
            if serializer.is_valid():
                serializer.save()
                data["success"] = "update sucessful"
                return Response(data=data)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST )