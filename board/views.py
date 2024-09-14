from django.shortcuts import render
from rest_framework.generics import (CreateAPIView, DestroyAPIView,
                                     ListAPIView, RetrieveAPIView,
                                     UpdateAPIView, get_object_or_404)
from rest_framework.permissions import IsAuthenticated

from board.models import Advertisement, Feedback
from board.paginators import AdvertisementPaginator
from board.serializers import FeedbackSerializer, AdvertisementSerializer
from users.permissions import IsModer, IsOwner


class FeedbackCreateAPIView(CreateAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    permission_classes = [IsAuthenticated,]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class FeedbackListAPIView(ListAPIView):
    queryset = Feedback.objects.all().order_by('-date')
    serializer_class = FeedbackSerializer
    permission_classes = [IsAuthenticated,]


class FeedbackUpdateAPIView(UpdateAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    permission_classes = [IsAuthenticated, IsModer | IsOwner]


class FeedbackDestroyAPIView(DestroyAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    permission_classes = [IsAuthenticated, IsModer | IsOwner]


class AdvertisementCreateAPIView(CreateAPIView):
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    permission_classes = [IsAuthenticated,]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class AdvertisementListAPIView(ListAPIView):
    queryset = Feedback.objects.all().order_by('-date')
    serializer_class = AdvertisementSerializer
    pagination_class = AdvertisementPaginator


class AdvertisementRetrieveAPIView(RetrieveAPIView):
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    permission_classes = [IsAuthenticated, ]


class AdvertisementUpdateAPIView(UpdateAPIView):
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    permission_classes = [IsAuthenticated, IsModer | IsOwner]


class AdvertisementDestroyAPIView(DestroyAPIView):
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    permission_classes = [IsAuthenticated, IsModer | IsOwner]
