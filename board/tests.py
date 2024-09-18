from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Advertisement, Feedback
from users.models import User


class AdvertisementTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(
            email="test@example.com", password="test123"
        )
        self.client.force_authenticate(user=self.user)
        self.advertisement = Advertisement.objects.create(title="Test Advertisement",
                                                          price=10,
                                                          description="This is a test advertisement.",
                                                          author=self.user)
        self.feedback = Feedback.objects.create(text="This is a test feedback",
                                                ad=self.advertisement,
                                                author=self.user)

    def test_advertisement_retrieve(self):
        url = reverse("board:advertisement-retrieve", args=(self.advertisement.pk,))
        self.data = {
                        "title": "Test Advertisement",
                        "price": 10,
                        "description": "This is a test advertisement.",
                        "author": self.user
                    }
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data['title'], self.advertisement.title)
        self.assertEqual(data['author'], self.user.id)

    def test_advertisement_create(self):
        self.url = reverse("board:advertisement-create")
        self.data = {
                        "title": "Test Advertisement 2",
                        "price": 20,
                        "author": self.user.id
                    }
        response = self.client.post(self.url, self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Advertisement.objects.all().count(), 2)
        self.assertEqual(response.data['author'], self.user.id)

    def test_advertisement_update(self):
        self.url = reverse("board:advertisement-update", args=(self.advertisement.pk,))
        self.data = {
                        "title": "Updated Test Advertisement",
                        "price": 15,
                        "author": self.user.id
                    }
        response = self.client.put(self.url, self.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.data['title'])

    def test_advertisement_delete(self):
        self.url = reverse("board:advertisement-delete", args=(self.advertisement.pk,))
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Advertisement.objects.all().count(), 0)

    # def test_advertisement_list(self):
    #     self.url = reverse("board:advertisement-list")
    #     response = self.client.get(self.url)
    #     data = response.json()
    #     dt = self.advertisement.created_at.isoformat()
    #     result = {
    #         "count": 1,
    #         "next": None,
    #         "previous": None,
    #         "results": [
    #             {
    #                 "id": self.advertisement.id,
    #                 "title": "Test Advertisement",
    #                 "price": 10,
    #                 "created_at": dt,
    #                 "count_of_feedback": 1,
    #                 "feedbacks": ['This is a test feedback'],
    #                 "description": "This is a test advertisement.",
    #                 "author": self.user.id
    #             }
    #         ]
    #     }
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertEqual(data, result)

    class FeedbackTestCase(APITestCase):
        def setUp(self):
            self.user = User.objects.create(
                email="test@example.com", password="test123"
            )
            self.client.force_authenticate(user=self.user)
            self.advertisement = Advertisement.objects.create(title="Test Advertisement",
                                                              price=10,
                                                              description="This is a test advertisement.",
                                                              author=self.user)
            self.feedback = Feedback.objects.create(text="This is a test feedback",
                                                    ad=self.advertisement,
                                                    author=self.user)

        def test_feedback_create(self):
            self.url = reverse("board:feedback-create")
            self.data = {
                            "text": "Test Feedback 2",
                            "author": self.user.id
                        }
            response = self.client.post(self.url, self.data)
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)
            self.assertEqual(Feedback.objects.all().count(), 2)
            self.assertEqual(response.data['author'], self.user.id)

        def test_feedback_update(self):
            self.url = reverse("board:feedback-update", args=(self.feedback.pk,))
            self.data = {
                            "text": "Updated Test Feedback",
                            "author": self.user.id
                        }
            response = self.client.put(self.url, self.data)
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertEqual(response.data['text'], self.data['text'])

        def test_feedback_delete(self):
            self.url = reverse("board:feedback-destroy", args=(self.feedback.pk,))
            response = self.client.delete(self.url)
            self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
            self.assertEqual(Feedback.objects.all().count(), 0)
