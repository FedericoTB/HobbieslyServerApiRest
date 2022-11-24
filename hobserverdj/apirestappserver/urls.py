from django.urls import include, path
from rest_framework import routers

from apirestappserver.views import *
from rest_framework_simplejwt import views as jwt_views
from apirestappserver.views import ChangePasswordView, LoginView, UpdateProfileView, UserRegistrationView

router = routers.DefaultRouter()
router.register(r'users',UserViewSet)
router.register(r'groups',UsersGroupsViewSet)
router.register(r'categories',CategoriesViewSet)
router.register(r'memberships',MembershipViewSet)
router.register(r'classifications',ClassificationViewSet)
router.register(r'rooms',RoomsViewSet)
router.register(r'messages',MessagesViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/', include('rest_framework.urls', namespace='rest_framework')),
    path("api/register/", UserRegistrationView.as_view(), name="register"),
    path("api/loginng/", LoginView.as_view(), name="loginng"),
    path("api/update-profile/<int:pk>/", UpdateProfileView.as_view(), name="update-profile"),
    path("api/change-password/<int:pk>/",ChangePasswordView.as_view(),name="change-password",),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]