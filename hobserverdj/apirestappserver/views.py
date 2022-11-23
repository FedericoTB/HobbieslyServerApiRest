from apirestappserver.models import *
from apirestappserver.serializers import *
from rest_framework import viewsets
from rest_framework import permissions
# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class UsersGroupsViewSet(viewsets.ModelViewSet):
    queryset = UsersGroups.objects.all()
    serializer_class = UsersGroupsSerializer
    permission_classes = [permissions.IsAuthenticated]

class CategoriesViewSet(viewsets.ModelViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer
    permission_classes = [permissions.IsAuthenticated]
    
class MembershipViewSet(viewsets.ModelViewSet):
    queryset = Membership.objects.all()
    serializer_class = MembershipsSerializer
    permission_classes = [permissions.IsAuthenticated]

class ClassificationViewSet(viewsets.ModelViewSet):
    queryset = Classification.objects.all()
    serializer_class = ClassificationsSerializer
    permission_classes = [permissions.IsAuthenticated]

class RoomsViewSet(viewsets.ModelViewSet):
    queryset = Rooms.objects.all()
    serializer_class = RoomsSerializer
    permission_classes = [permissions.IsAuthenticated]

class MessagesViewSet(viewsets.ModelViewSet):
    queryset = Messages.objects.all()
    serializer_class = MessagesSerializer
    permission_classes = [permissions.IsAuthenticated]