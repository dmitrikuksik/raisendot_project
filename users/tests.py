# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from .serializers import UserSerializer, UserRegistrationSerializer
from .models import User
from .views import UserLogin, UserRegistration
from rest_framework.authtoken.models import Token


class SerializerTest(TestCase):

    def test_login(self):
        user = User.objects.create()
        user.email = 'olek@mail.pl'
        user.set_password('haslo')
        user.save()
        request = self.client.post('/login/',{'email':user.email,'password': 'haslo'})
        token = Token.objects.get(user=user)
        self.assertEqual(token.key,request.data['token'])

    def test_login_wrong(self):
        user = User.objects.create()
        user.email = 'olek@mail.pl'
        user.set_password('haslo')
        user.save()
        request = self.client.post('/login/',{'email':user.email,'password': 'hslo'})
        self.assertEqual(request.status_code, 401)

    def test_registration(self):
        request = self.client.post('/register/',{'email':'olek@mail.pl','username':'olek','password':'haslo','password2':'haslo'})
        user = User.objects.get(email = 'olek@mail.pl')
        token = Token.objects.get(user = user)
        self.assertEqual(token.key, request.data['token'] )

    def test_my_information(self):
        user = User.objects.create()
        user.email = 'olek@mail.pl'
        user.username = 'olek'
        user.set_password('haslo')
        user.save()

        request = self.client.post('/login/',{'email':user.email,'password':'haslo'})
        token = request.data['token']

        request = self.client.get('/users/me/')
        user = User.objects.get(email=request.data['email'])

        token_to_verify = Token.objects.get(user=user)
        self.assertEqual(token, token_to_verify.key)

    def test_user_list(self):
        user = User.objects.create()
        user.email = 'olek@mail.pl'
        user.username = 'olek'
        user.set_password('haslo')
        user.save()

        user = User.objects.create()
        user.email = 'bolek@mail.pl'
        user.username = 'bolek'
        user.set_password('haslo')
        user.save()

        request = self.client.get('/users/')
        self.assertEqual(len(request.data),len(User.objects.all()))

    def test_logout(self):
        user = User.objects.create()
        user.email = 'olek@mail.pl'
        user.username = 'olek'
        user.set_password('haslo')
        user.save()

        request = self.client.post('/login/',{'email':user.email,'password':'haslo'})
        token = request.data['token']

        request = self.client.post('/logout/')
        is_exist = Token.objects.filter(user = user).exists()
        self.assertEqual(is_exist,False)
