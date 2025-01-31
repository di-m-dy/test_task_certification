from django.urls import path

from users.apps import UsersConfig
from users.views import UserListAPIView, UserRetrieveAPIView, UserCreateAPIView, UserUpdateAPIView, UserDestroyAPIView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

app_name = UsersConfig.name

urlpatterns = [
    path('', UserListAPIView.as_view(), name='user-list'),
    path('<int:pk>/', UserRetrieveAPIView.as_view(), name='user-retrieve'),
    path('create/', UserCreateAPIView.as_view(), name='user-create'),
    path('<int:pk>/update/', UserUpdateAPIView.as_view(), name='user-update'),
    path('<int:pk>/delete/', UserDestroyAPIView.as_view(), name='user-delete'),
    # jwt
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
