from django.urls import include, path
from rest_framework import routers

from apirestappserver.views import *
from rest_framework_simplejwt import views as jwt_views
from apirestappserver.views import ChangePasswordView, LoginView, UpdateProfileView, UserRegistrationView

from drf_yasg import openapi
from drf_yasg.views import get_schema_view as swagger_get_schema_view

router = routers.DefaultRouter()
router.register(r'users',UserViewSet)
router.register(r'usergroups',UsersGroupsViewSet)
router.register(r'categories',CategoriesViewSet)
router.register(r'memberships',MembershipViewSet)
router.register(r'classifications',ClassificationViewSet)
router.register(r'rooms',RoomsViewSet)
router.register(r'messages',MessagesViewSet)

schema_view = swagger_get_schema_view(
    openapi.Info(
        title="Hobbiesly Server Api Rest",
        default_version="1.0.0",
        description="API documentation of Hobbiesly Server",
    ),
    public=True,
)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/rooms/by-group/<int:group_id>/',RoomOfGroupViewSet.as_view(),name="rooms-of-group"),
    path('api/messages/by-room/<int:room_id>/',MessagesOfRoomViewSet.as_view(),name="messages-of-room"),
    path("api/register/", UserRegistrationView.as_view(), name="register"),
    path("api/loginng/", LoginView.as_view(), name="loginng"),
    path("api/update-profile/<int:pk>/", UpdateProfileView.as_view(), name="update-profile"),
    path("api/change-password/<int:pk>/",ChangePasswordView.as_view(),name="change-password",),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('api/docs/', schema_view.with_ui('swagger', cache_timeout=0), name="swagger-schema"),
   
]