from django.urls import include, path
from rest_framework import routers
from api import views
from comments import views
from commentsboard import views
from django.contrib import admin
from board import views


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path("api/v1/foods/", include("api.urls")),
    path("admin/", admin.site.urls),
    path("usrs/v1/", include("users.urls")),
    path("commentsfood/v1/", include("comments.urls")),
    path("board/v1/", include("board.urls")),
    path("commentsboard/v1/", include("commentsboard.urls")),
]