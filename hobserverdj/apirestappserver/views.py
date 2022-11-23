from rest_framework import viewsets

from django.contrib.auth import get_user_model
from rest_framework import generics, status
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

class UsersGroupsViewSet(viewsets.ModelViewSet):
    queryset = UsersGroups.objects.all()
    serializer_class = UsersGroupsSerializer
    permission_classes = (IsAuthenticated,)

class CategoriesViewSet(viewsets.ModelViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer
    permission_classes = (IsAuthenticated,)
    
class MembershipViewSet(viewsets.ModelViewSet):
    queryset = Membership.objects.all()
    serializer_class = MembershipsSerializer
    permission_classes = (IsAuthenticated,)

class ClassificationViewSet(viewsets.ModelViewSet):
    queryset = Classification.objects.all()
    serializer_class = ClassificationsSerializer
    permission_classes = (IsAuthenticated,)

class RoomsViewSet(viewsets.ModelViewSet):
    queryset = Rooms.objects.all()
    serializer_class = RoomsSerializer
    permission_classes = (IsAuthenticated,)

class MessagesViewSet(viewsets.ModelViewSet):
    queryset = Messages.objects.all()
    serializer_class = MessagesSerializer
    permission_classes = (IsAuthenticated,)