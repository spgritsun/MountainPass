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
    levels = LevelSerializer()
    images = ImageSerializer()
    statuses = StatusSerializer(default={'status_name': 'new'})

    class Meta:
        model = Pass
        fields = '__all__'

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        coords_data = validated_data.pop('coords')
        levels_data = validated_data.pop('levels')
        images_data = validated_data.pop('images')
        statuses_data = validated_data.pop('statuses')
        user_instance, _ = User.objects.get_or_create(**user_data)
        coords_instance, _ = Coordinates.objects.get_or_create(**coords_data)
        levels_instance, _ = Level.objects.get_or_create(**levels_data)
        images_instance, _ = Image.objects.get_or_create(**images_data)
        statuses_instance, _ = Status.objects.get_or_create(**statuses_data)
        pass_instance = Pass.objects.create(user=user_instance, coords=coords_instance, levels=levels_instance,
                                            images=images_instance, statuses=statuses_instance, **validated_data)
        return pass_instance
