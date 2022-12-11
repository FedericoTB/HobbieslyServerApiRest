from rest_framework import viewsets

from django.contrib.auth import get_user_model
from rest_framework import generics, status, filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView

from apirestappserver.models import *
from apirestappserver.serializers import *

# Create your views here.

class UserRegistrationView(generics.CreateAPIView):
    """
    User registration view.
    """

    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        """
        Post request to register a user
        """
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(
            {
                "User": UserSerializer(user).data,
            },
            status=status.HTTP_201_CREATED,
        )

class LoginView(TokenObtainPairView):
    """
    Client login endpoint.
    """

    serializer_class = LoginSerializer

class UpdateProfileView(generics.UpdateAPIView):
    """
    An endpoint to update the profile of a logged-in user
    """

    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = UpdateUserSerializer

class ChangePasswordView(generics.UpdateAPIView):
    """
    A view to change the password of a user.
    """

    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = ChangePasswordSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = [filters.SearchFilter]
    search_fields = ["id", "username"]

class UsersGroupsViewSet(viewsets.ModelViewSet):
    queryset = UsersGroups.objects.all()
    serializer_class = UsersGroupsSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = [filters.SearchFilter]
    search_fields = ["id", "name","owner"]

class CategoriesViewSet(viewsets.ModelViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = [filters.SearchFilter]
    search_fields = ["id","name"]
    
class MembershipViewSet(viewsets.ModelViewSet):
    queryset = Membership.objects.all()
    serializer_class = MembershipsSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = [filters.SearchFilter]
    search_fields = ["id",]

class ClassificationViewSet(viewsets.ModelViewSet):
    queryset = Classification.objects.all()
    serializer_class = ClassificationsSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = [filters.SearchFilter]
    search_fields = ["id",]

class RoomsViewSet(viewsets.ModelViewSet):
    queryset = Rooms.objects.all()
    serializer_class = RoomsSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = [filters.SearchFilter]
    search_fields = ["id","name","group","owner"]

class RoomOfGroupViewSet(generics.ListAPIView):
    serializer_class = RoomsSerializer
    permission_classes = (IsAuthenticated,)
    
    def get_queryset(self):
        queryset = Rooms.objects.all()
        gid = self.kwargs["group_id"]
        if gid is not None:
            queryset = Rooms.objects.filter(group = gid)
            
        return queryset

class MessagesViewSet(viewsets.ModelViewSet):
    queryset = Messages.objects.all()
    serializer_class = MessagesSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = [filters.SearchFilter,filters.OrderingFilter,]
    search_fields = ["id","name","room","owner"]
    ordering = ('created_at',)

class MessagesOfRoomViewSet(generics.ListAPIView):
    serializer_class = MessagesSerializer

    def get_queryset(self):
        queryset = Messages.objects.all().order_by('created_at')
        rid = self.kwargs["room_id"]
        if rid is not None:
            queryset = Messages.objects.filter(room = rid)
        return queryset