from rest_framework.relations import SlugRelatedField, StringRelatedField, PrimaryKeyRelatedField
from rest_framework.serializers import ModelSerializer
from main.models import *


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class CoordSerializer(ModelSerializer):
    class Meta:
        model = Coordinates
        fields = '__all__'


class ImageSerializer(ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'


class LevelSerializer(ModelSerializer):
    class Meta:
        model = Level
        fields = '__all__'


class StatusSerializer(ModelSerializer):
    class Meta:
        model = Status
        fields = '__all__'


class PassSerializer(ModelSerializer):
    user = UserSerializer()
    coords = CoordSerializer()
    images = ImageSerializer()
    levels = LevelSerializer()
    statuses = StatusSerializer()

    class Meta:
        model = Pass
        fields = '__all__'

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user_instance, _ = User.objects.get_or_create(**user_data)
        pass_instance = Pass.objects.create(user=user_instance, **validated_data)
        return pass_instance
