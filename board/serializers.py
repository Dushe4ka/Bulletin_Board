from board.models import Advertisement, Feedback
from rest_framework.serializers import ModelSerializer, SerializerMethodField


class FeedbackSerializer(ModelSerializer):
    class Meta:
        model = Feedback
        fields = "__all__"


class AdvertisementSerializer(ModelSerializer):
    count_of_feedback = SerializerMethodField()
    feedbacks = SerializerMethodField()

    def get_count_of_feedback(self, advertisement):
        return advertisement.feedbacks.count()

    def get_feedbacks(self, advertisement):
        feedback_set = Feedback.objects.filter(ad=advertisement.id)
        return [feedback.text for feedback in feedback_set]

    class Meta:
        model = Advertisement
        fields = ("title", "price", "author", "count_of_feedback", "feedbacks", "created_at")
