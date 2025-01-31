from rest_framework.serializers import ModelSerializer

from users.models import User


class UserSerializer(ModelSerializer):
    """
    Сериализатор для пользователя
    """

    class Meta:
        model = User
        fields = '__all__'


class UserListSerializer(ModelSerializer):
    """
    Сериализатор для списка пользователей
    """

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name')


class UserCreateSerializer(ModelSerializer):
    """
    Сериализатор для создания пользователя
    """
    class Meta:
        model = User
        fields = ('email', 'password')


class UserUpdateSerializer(ModelSerializer):
    """
    Сериализатор для обновления данных пользователя
    """

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'date_joined', 'last_login')
        read_only_fields = ('date_joined', 'last_login')


class UserDestroySerializer(ModelSerializer):
    """
    Сериализатор для удаления пользователя
    """

    class Meta:
        model = User
        fields = ('id', 'email')
        read_only_fields = ('id', 'email')
