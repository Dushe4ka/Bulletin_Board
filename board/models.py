from django.db import models
from users.models import User

NULLABLE = {"blank": True, "null": True}


class Advertisement(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Название объявления",
        help_text="Укажите название объявления",
    )
    price = models.PositiveIntegerField(
        verbose_name="Цена объявления",
        help_text="Укажите цену объявления",
    )
    description = models.TextField(
        verbose_name="Описание объявления",
        help_text="Укажите описание объявления",
        **NULLABLE
    )
    author = models.ForeignKey(
        User,
        verbose_name='Автор объявления',
        on_delete=models.CASCADE,
        help_text='Укажите владельца привычки',
        related_name="author"
    )
    created_at = models.DateTimeField(
        verbose_name='дата создания',
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.title},  {self.price} -  {self.author}"

    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"


class Feedback(models.Model):
    text = models.TextField(
        verbose_name='Отзыв',
        help_text='Укажите отзыв',
    )
    author = models.ForeignKey(
        User,
        verbose_name='Автор отзыва',
        on_delete=models.CASCADE,
        help_text='Укажите автора отзыва',
        related_name="feedback_author"
    )
    ad = models.ForeignKey(
        Advertisement,
        verbose_name='Объявление',
        on_delete=models.CASCADE,
        help_text='Укажите объявление',
        related_name="feedbacks"
    )
    created_at = models.DateTimeField(
        verbose_name='дата создания',
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.text} -  {self.ad}"

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"

