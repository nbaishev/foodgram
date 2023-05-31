from djoser.serializers import UserCreateSerializer, UserSerializer
from rest_framework.fields import SerializerMethodField

from users.models import User
from users.validators import validate_username


class CustomUserCreateSerializer(UserCreateSerializer):
    """Сериализатор для создания пользователя."""

    class Meta:
        model = User
        fields = tuple(User.REQUIRED_FIELDS) + (
            User.USERNAME_FIELD,
            'password',
        )

    def validate_username(self, value):
        return validate_username(value)

    def create(self, validated_data):
        user = User.objects.create(
            email=validated_data['email'],
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class CustomUserSerializer(UserSerializer):
    """Сериализатор для пользователя."""

    is_subscribed = SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = (
            'email',
            'id',
            'username',
            'first_name',
            'last_name',
            'is_subscribed',
        )

    def get_is_subscribed(self, obj):
        user = self.context.get('request').user
        if user.is_anonymous:
            return False
        return user.subscriber.filter(author=obj).exists()
