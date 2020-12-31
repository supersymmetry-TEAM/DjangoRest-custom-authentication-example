# django-rest-token-authentication-app


this is quick api code for DjangoRest token authentication.

The authentication.py file overriied BaseAuthentication.

you should add avobe code in setting.py

!Note! : you should change yourappname 

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "yourappname.authentication.JWTAuthentication",
    ],
}

INSTALLED_APPS = [
 ...,
    'yourappname.apps.YourappnameConfig',
 ...,
 ...
]
