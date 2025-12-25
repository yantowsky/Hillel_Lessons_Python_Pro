import jwt
from datetime import datetime, timedelta
from django.conf import settings

def create_access_token(user_id):
    payload = {
        'user_id': user_id,
        'type': 'access',
        'exp': datetime.utcnow() + settings.JWT_SETTINGS['ACCESS_TOKEN_LIFETIME'],
        'iat': datetime.utcnow()
    }
    return jwt.encode(
        payload,
        settings.JWT_SETTINGS['SIGNING_KEY'],
        algorithm=settings.JWT_SETTINGS['ALGORITHM']
    )


def create_refresh_token(user_id):
    payload = {
        'user_id': user_id,
        'type': 'refresh',
        'exp': datetime.utcnow() + settings.JWT_SETTINGS['REFRESH_TOKEN_LIFETIME'],
        'iat': datetime.utcnow()
    }
    return jwt.encode(
        payload,
        settings.JWT_SETTINGS['SIGNING_KEY'],
        algorithm=settings.JWT_SETTINGS['ALGORITHM']
    )


def decode_token(token):
    return jwt.decode(
        token,
        settings.JWT_SETTINGS['SIGNING_KEY'],
        algorithms=[settings.JWT_SETTINGS['ALGORITHM']]
    )
