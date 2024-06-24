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
        user_instance, _ = User.objects.get_or_create(email=user_data['email'], defaults=user_data)
        coords_instance, _ = Coordinates.objects.get_or_create(**coords_data)
        levels_instance, _ = Level.objects.get_or_create(**levels_data)
        images_instance, _ = Image.objects.get_or_create(**images_data)
        statuses_instance, _ = Status.objects.get_or_create(**statuses_data)
        pass_instance = Pass.objects.create(user=user_instance, coords=coords_instance, levels=levels_instance,
                                            images=images_instance, statuses=statuses_instance, **validated_data)
        return pass_instance

    def update(self, instance, validated_data):
        try:
            if validated_data.get('statuses')['status_name'] == 'new':
                # Обновление основного объекта Pass
                instance.beauty_title = validated_data.get('beauty_title', instance.beauty_title)
                instance.title = validated_data.get('title', instance.title)
                instance.other_titles = validated_data.get('other_titles', instance.other_titles)
                instance.connect = validated_data.get('connect', instance.connect)
                instance.add_time = validated_data.get('add_time', instance.add_time)
                instance.save()

                # Обновление связанных объектов

                coords_data = validated_data.get('coords')
                if coords_data:
                    coords_serializer = self.fields['coords']
                    coords_instance = instance.coords
                    coords_serializer.update(coords_instance, coords_data)

                images_data = validated_data.get('images')
                if images_data:
                    images_serializer = self.fields['images']
                    images_instance = instance.images
                    images_serializer.update(images_instance, images_data)

                levels_data = validated_data.get('levels')
                if levels_data:
                    levels_serializer = self.fields['levels']
                    levels_instance = instance.levels
                    levels_serializer.update(levels_instance, levels_data)

                return instance
            else:
                return instance
        except Exception as e:
            raise RuntimeError(f'Ошибка при обновлении записи: {str(e)}')

