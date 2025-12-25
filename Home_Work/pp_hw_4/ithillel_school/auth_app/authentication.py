from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth.models import User
import jwt
from django.conf import settings
from .jwt_utils import decode_token


class JWTAuthentication(BaseAuthentication):
    def authenticate(self, request):
        auth_header = request.headers.get('Authorization')

        if not auth_header:
            return None

        try:
            prefix, token = auth_header.split()
            if prefix.lower() != 'bearer':
                raise AuthenticationFailed('Invalid token prefix')

            payload = decode_token(token)

            if payload.get('type') != 'access':
                raise AuthenticationFailed('Invalid token type')

            user = User.objects.get(id=payload['user_id'])
            return (user, token)

        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Token expired')

        except Exception:
            raise AuthenticationFailed('Invalid token')
