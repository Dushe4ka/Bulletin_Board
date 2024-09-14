import os

from django.core.mail import send_mail
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated

from config import settings
from users.models import User
from users.serializers import UserSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import update_session_auth_hash
from .serializers import ChangePasswordSerializer
# ResetPasswordRequestSerializer, ResetPasswordSerializer

from django.contrib.auth.tokens import PasswordResetTokenGenerator
from rest_framework.response import Response


class UserCreateAPIView(generics.GenericAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def change_password(request):
    if request.method == 'POST':
        serializer = ChangePasswordSerializer(data=request.data)
        if serializer.is_valid():
            user = request.user
            if user.check_password(serializer.data.get('old_password')):
                user.set_password(serializer.data.get('new_password'))
                user.save()
                update_session_auth_hash(request, user)  # To update session after password change
                return Response({'message': 'Password changed successfully.'}, status=status.HTTP_200_OK)
            return Response({'error': 'Incorrect old password.'}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
# class RequestPasswordReset(generics.GenericAPIView):
#     permission_classes = [AllowAny]
#     serializer_class = ResetPasswordRequestSerializer
#
#     def post(self, request):
#         serializer = self.serializer_class(data=request.data)
#         email = request.data['email']
#         user = User.objects.filter(email__iexact=email).first()
#
#         if user:
#             token_generator = PasswordResetTokenGenerator()
#             token = token_generator.make_token(user)
#             reset = PasswordReset(email=email, token=token)
#             reset.save()
#
#             host = self.request.get_host()
#             url = f'http://{host}/users/email-confirm/{token}/'
#             send_mail(
#                 subject='Изменение пароля',
#                 message=f'Для изменения пароля перейдите по ссылке {url}',
#                 from_email=settings.EMAIL_HOST_USER,
#                 recipient_list=[user.email],
#             )
#
#             return Response({'success': 'We have sent you a link to reset your password'}, status=status.HTTP_200_OK)
#         else:
#             return Response({"error": "User with credentials not found"}, status=status.HTTP_404_NOT_FOUND)
#
#
# class ResetPassword(generics.GenericAPIView):
#     serializer_class = ResetPasswordSerializer
#     permission_classes = []
#
#     def post(self, request, token):
#         serializer = self.serializer_class(data=request.data)
#
#         serializer.is_valid(raise_exception=True)
#         data = serializer.validated_data
#
#         new_password = data['new_password']
#         confirm_password = data['confirm_password']
#
#         if new_password != confirm_password:
#             return Response({"error": "Passwords do not match"}, status=400)
#
#         reset_obj = PasswordReset.objects.filter(token=token).first()
#
#         if not reset_obj:
#             return Response({'error': 'Invalid token'}, status=400)
#
#         user = User.objects.filter(email=reset_obj.email).first()
#
#         if user:
#             user.set_password(request.data['new_password'])
#             user.save()
#
#             reset_obj.delete()
#
#             return Response({'success': 'Password updated'})
#         else:
#             return Response({'error': 'No user found'}, status=404)

