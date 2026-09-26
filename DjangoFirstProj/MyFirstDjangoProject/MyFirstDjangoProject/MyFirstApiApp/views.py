from django.contrib.admin import action
from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from MyFirstDjangoProject.MyFirstApiApp.serializers import GroupSerializer, UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=False, methods=["get"], url_path="getSaadiUsers")
    def get_saadi_users(self, request):
        queryset = User.objects.filter(username__icontains="saadi")
        x =queryset.values("username", "email", "first_name", "last_name").__str__()
        return Response({
            "message": x  
        })

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """

    queryset = Group.objects.all().order_by("name")
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]