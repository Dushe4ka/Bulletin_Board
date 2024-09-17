from django.urls import path

from board.apps import BoardConfig
from board.views import (AdvertisementListAPIView, AdvertisementRetrieveAPIView, AdvertisementDestroyAPIView,
                         AdvertisementCreateAPIView, AdvertisementUpdateAPIView, FeedbackListAPIView,
                         FeedbackCreateAPIView, FeedbackUpdateAPIView, FeedbackDestroyAPIView)

app_name = BoardConfig.name

urlpatterns = [
    path("", AdvertisementListAPIView.as_view(), name="advertisement-list"),
    path("<int:pk>/retrieve/", AdvertisementRetrieveAPIView.as_view(), name="advertisement-retrieve"),
    path("create/", AdvertisementCreateAPIView.as_view(), name="advertisement-create"),
    path("<int:pk>/update/", AdvertisementUpdateAPIView.as_view(), name="advertisement-update"),
    path("<int:pk>/delete/", AdvertisementDestroyAPIView.as_view(), name="advertisement-delete"),
    path("feedback/create", FeedbackCreateAPIView.as_view(), name="feedback-create"),
    path("feedback/<int:pk>/destroy", FeedbackDestroyAPIView.as_view(), name="feedback-destroy"),
    path("feedback/<int:pk>/update", FeedbackUpdateAPIView.as_view(), name="feedback-update"),
    path("feedback/", FeedbackListAPIView.as_view(), name="feedback-list"),
]