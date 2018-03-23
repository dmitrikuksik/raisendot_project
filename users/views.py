# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json

from django.shortcuts import render
from django.contrib.auth import login,logout,authenticate
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework import viewsets

from .models import User
from .serializers import UserSerializer, UserRegistrationSerializer, UserSerializerInfo


class UserRegistration(APIView):
    authentication_classes = (authentication.SessionAuthentication,authentication.BasicAuthentication,)
    permission_classes = (AllowAny,)
    serializer_class = UserRegistrationSerializer

    def post(self, request, format='JSON'):
        serializer = UserRegistrationSerializer(data = request.POST)
        if serializer.is_valid(raise_exception=True):
            new_user = serializer.save()
            token = Token.objects.create(user=new_user)
            return Response({'token':token.key})
        return Response(status=status.HTTP_404_NOT_FOUND)

class UserLogin(APIView):
    authentication_classes = (authentication.SessionAuthentication,authentication.BasicAuthentication,)
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer

    def post(self, request, format='JSON'):
        serializer = UserSerializer(data = request.POST)
        if serializer.is_valid():
            auth_user = authenticate(email=serializer.data['email'],password=serializer.data['password'])
            login(request,auth_user)
            token = Token.objects.get_or_create(user=auth_user)
            return Response({'token':token[0].key})
        return Response(status=status.HTTP_404_NOT_FOUND)

class UserMe(APIView):
    authentication_classes = (authentication.SessionAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializerInfo

    def get(self, request, format='JSON'):
        try:
            user = User.objects.get(email=request.user.email)
            if user.is_authenticated():
                serializer = UserSerializerInfo(user)
                return Response(serializer.data)
        except:
            pass
        return Response(status=status.HTTP_404_NOT_FOUND)

class UserList(APIView):
    authentication_classes = (authentication.BasicAuthentication,)
    permission_classes = (AllowAny,)
    serializer_class = UserSerializerInfo

    def get(self,request, fofrmat='JSON'):
        try:
            queryset = User.objects.all()
        except:
            pass
        serializer = UserSerializerInfo(queryset,many = True)

        return Response(serializer.data)

class UserLogout(APIView):
    authentication_classes = (authentication.SessionAuthentication,)
    permission_classes = (AllowAny,)

    def post(self,request):
        return self.logout(request)

    def logout(self,request):
        try:
            Token.objects.get(user=request.user).delete()
        except:
            pass

        logout(request)
        return Response({"success": _("Successfully logged out.")},
                    status=status.HTTP_200_OK)
