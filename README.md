# django-rest-custom-authentication-example


This is example if custom authentication.

The authentication.py file override override the .authenticate(self, request) method.

You should add authentication.py to the foler with setting.py

and below code in setting.py 

!Note! : you should change yourappname 



REST_FRAMEWORK = 

{
    
    "DEFAULT_AUTHENTICATION_CLASSES": [
    
    "yourappname.authentication.JWTAuthentication",
        
    ],
}


INSTALLED_APPS = 
[

 ...,
 
 ...,
 
    'yourappname.apps.YourappnameConfig',
    
 ...,
 
 ...
 
]

 
