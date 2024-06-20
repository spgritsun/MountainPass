from rest_framework.relations import SlugRelatedField, StringRelatedField, PrimaryKeyRelatedField
from rest_framework.serializers import ModelSerializer
from main.models import Pass, User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class PassSerializer(ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Pass
        fields = '__all__'

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user_instance, _ = User.objects.get_or_create(**user_data)
        pass_instance = Pass.objects.create(user=user_instance, **validated_data)
        return pass_instance
