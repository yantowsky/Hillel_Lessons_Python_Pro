from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from .jwt_utils import create_access_token, create_refresh_token, decode_token
import jwt


class LoginView(APIView):
    permission_classes = []

    def post(self, request):
        user = authenticate(
            username=request.data.get('username'),
            password=request.data.get('password')
        )

        if not user:
            return Response({'error': 'Invalid credentials'}, status=401)

        return Response({
            'access': create_access_token(user.id),
            'refresh': create_refresh_token(user.id)
        })


class RefreshTokenView(APIView):
    permission_classes = []

    def post(self, request):
        refresh_token = request.data.get('refresh')

        try:
            payload = decode_token(refresh_token)

            if payload.get('type') != 'refresh':
                return Response({'error': 'Invalid refresh token'}, status=401)

            new_access = create_access_token(payload['user_id'])

            return Response({'access': new_access})

        except jwt.ExpiredSignatureError:
            return Response({'error': 'Refresh token expired'}, status=401)
