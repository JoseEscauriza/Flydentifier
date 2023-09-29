# basic test class + request generator
from django.test import TestCase, RequestFactory
# for failed authentication test
from django.contrib.auth.models import AnonymousUser
from django.urls import reverse  # for reverse-lookup on url names
from apps.user import views, models


class TestUserView(TestCase):
    pass
