from django.shortcuts import render,redirect, get_object_or_404
from django.http  import HttpResponse
from .serializers import *
from .models import Profile
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model
User = get_user_model()
from .permissions import IsCompanyAdmin, IsNormalUser,IsVendor, UserIsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from rest_framework.decorators import APIView
from rest_framework.response import Response
from .models import *

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


class BookingsList(APIView):
    """
    List all Bookings, or Create a booking
    """
    def get(self, request, format=None):
        book = Bookings.objects.all()
        serializer = BookingsSerializer(book, many=True)
        return Response(serializer.data)
    
    def post(self,request, format=None):
        serializer= BookingsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookingDetail(APIView):
    """
    Retrieve, update or delete a booking instance
    """
    def get_object(self, pk):
        try:
            return Bookings,objects.get(pk=pk)
        except Bookings.DoesNotExist:
            raise Http404 
    
    def get(self, request, pk, format=None):
        book = self.get_object(pk)
        serializer = BookingsSerializer(book)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        book = self.get_object(pk)
        serializer = BookingsSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        book = self.get_object(pk)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)





