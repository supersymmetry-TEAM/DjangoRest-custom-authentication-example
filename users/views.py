import jwt
from django.conf import settings
from django.contrib.auth import authenticate


from rest_framework.permissions import IsAdminUser, AllowAny
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import api_view
from rest_framework.decorators import action
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

# from api.models import FoodDatas
# from api.serializer import FoodSerializer
# from comments.models import FoodComments
# from comments.serializer import FoodCommentSerializer

from .permission import IsSelf 
from .models import User
from .serializer import UserSerializer, UserInfoSerializer



class UsersViewSet(ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        permission_classes = []
        if self.action == "list":
            permission_classes = [IsSelf]
            # permission_classes = [IsAdminUser]
        elif (
            self.action == "create"
            or self.action == "retrieve"
            or self.action == "favs_api"
            or self.action == "favs_comments"
        ):            
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsSelf]

        return [permission() for permission in permission_classes]
  

    @action(detail=False, methods=["post"])
    def login(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        if not username or not password:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        user = authenticate(username=username, password=password)
        if user is not None:
            encoded_jwt = jwt.encode(
                {"pk": user.pk}, settings.SECRET_KEY, algorithm="HS256"
            )
            return Response(data={"token": encoded_jwt, "id": user.pk})
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
    
    @action(detail=True, methods=["put","get"])
    def info(self, request,pk):
        serializer = UserInfoSerializer(request.user, 
        data=request.data, partial=True,
        context={"request": request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_401_UNAUTHORIZED)
  


# example ~!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#     @action(detail=True)
#     def favs_api(self, request, pk):
#         user = self.get_object()
#         serializer = FoodSerializer(user.favs_api.all(), many=True, context={"request": request}).data
#         return Response(serializer)
    
#     @favs_api.mapping.put
#     def toggle_favs_api(self, request, pk):
#         pk = request.data.get("pk", None)
#         user = self.get_object()
#         if pk is not None:
#             try:
#                 food = FoodDatas.objects.get(pk=pk)
#                 if food in user.favs_api.all():
#                     user.favs_api.remove(food)
#                 else:
#                     user.favs_api.add(food)
#                 return Response()
#             except FoodDatas.DoesNotExist:
#                 pass
#         return Response(status=status.HTTP_400_BAD_REQUEST)
    # @action(detail=True)
    # def favs_comments(self, request, pk):
    #     user = self.get_object()
    #     serializer = CommentSerializer(user.favs_comments.all(), many=True, context={"request": request}).data
    #     return Response(serializer)
    
    # @favs_comments.mapping.put
    # def toggle_favs_comments(self, request, pk):
    #     pk = request.data.get("pk", None)
    #     user = self.get_object()
    #     if pk is not None:
    #         try:
    #             comment = Comments.objects.get(pk=pk)
    #             if comment in user.favs_comments.all():
    #                 user.favs_comments.remove(comment)
    #             else:
    #                 user.favs_comments.add(comment)
    #             return Response()
    #         except Comments.DoesNotExist:
    #             pass
    #     return Response(status=status.HTTP_400_BAD_REQUEST)

