import jwt
from django.conf import settings
from rest_framework import authentication
from users.models import User
from django.cotnrib.auth.models import User

class JWTBaseAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        try:
            token = request.META.get("HTTP_AUTHORIZATION") # check token with in header
            if token is None:
                return None
            _, jwt_token = token.split(" ") # the token generally is sended Basic + token or Bear + token so we need to parse
            decoded = jwt.decode(jwt_token, settings.SECRET_KEY, algorithms=["HS256"]) #decode the token
            pk = decoded.get("pk") 
            user = User.objects.get(pk=pk) 
            return (user, None) 
        except (ValueError, jwt.exceptions.DecodeError, User.DoesNotExist):
            return None
