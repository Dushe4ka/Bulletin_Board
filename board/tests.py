from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Advertisement, Feedback
from users.models import User


# class AdvertisementTestCase(APITestCase):
#     def setUp(self):
#         self.user = User.objects.create(email="test@example.com")
#         self.advertisement = Advertisement.objects.create(title="Test Advertisement",
#                                                           description="This is a test advertisement.",
#                                                           author=self.user)
