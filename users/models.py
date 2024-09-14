from django.db import models
from django.contrib.auth.models import AbstractUser

NULLABLE = {"blank": True, "null": True}


class User(AbstractUser):
    username = None

    class Type_role(models.TextChoices):
        user = 'Юзер'
        admin = 'Администратор'

    email = models.EmailField(
        unique=True,
        verbose_name="Почта",
        help_text="Укажите почту"
    )

    phone = models.CharField(
        max_length=35,
        verbose_name="Телефон",
        help_text="Укажите телефон",
        **NULLABLE
    )

    image = models.ImageField(
        upload_to="users/avatars",
        verbose_name="Аватар",
        help_text="Укажите аватар",
        **NULLABLE
    )

    first_name = models.CharField(
        max_length=30,
        verbose_name="Имя",
        help_text="Укажите имя",
        **NULLABLE
    )

    last_name = models.CharField(
        max_length=30,
        verbose_name="Фамилия",
        help_text="Укажите фамилию",
        **NULLABLE
    )

    role = models.CharField(
        choices=Type_role.choices,
        max_length=20,
        verbose_name="Роль",
        help_text="Укажите роль пользователя",
        **NULLABLE
    )

    image = models.ImageField(
        upload_to="users/image/",
        blank=True,
        null=True,
        verbose_name="Аватар",
        help_text="Загрузите аватар",
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"




