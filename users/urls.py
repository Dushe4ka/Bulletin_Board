from django.urls import path
from rest_framework.permissions import AllowAny
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.contrib.auth.views import LogoutView, PasswordChangeView, PasswordChangeDoneView, PasswordResetView, \
    PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from users.apps import UsersConfig
from users.views import UserCreateAPIView, change_password

app_name = UsersConfig.name
router = DefaultRouter()

urlpatterns = [
    path('register/', UserCreateAPIView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(permission_classes=(AllowAny,)), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(permission_classes=(AllowAny,)), name='token_refresh'),
    path('change_password/', change_password, name='change_password'),
    # path('password-reset/', PasswordResetView.as_view, name='password_reset'),
    # path('password-reset/done/', PasswordResetDoneView.as_view, name='password_reset_done'),
    # path('password-reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view, name='password_reset_confirm'),
    # path('password-reset/complete/', PasswordResetCompleteView.as_view, name='password_reset_complete'),
] + router.urls
