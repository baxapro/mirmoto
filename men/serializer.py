import io

from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from .models import Men



class MenSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model= Men
        fields = ("__all__")

# class MenModel:
#     def __init__(self,title,content):
#         self.title = title
#         self.content = content


    # title = serializers.CharField(max_length=255)
    # content = serializers.CharField()
    # slug = serializers.SlugField(max_length=255)
    # photo = serializers.ImageField()
    # time_create = serializers.DateTimeField(read_only=True)
    # time_update = serializers.DateTimeField(read_only=True)
    # is_published = serializers.BooleanField(default=True)
    # cat = serializers.CharField()
    # content1 = serializers.CharField()
    # content2 = serializers.CharField()

    # def create(self,validated_data):
    #     return Men.objects.create(**validated_data)
    #
    # def update(self,instance, validated_data):
    #     instance.title= validated_data.get("title",instance.title)
    #     instance.content = validated_data.get("content", instance.content)
    #     instance.cat_id = validated_data.get("cat_id", instance.cat_id)
    #     instance.content1 = validated_data.get("content1", instance.content1)
    #     instance.content2 = validated_data.get("content2", instance.content2)
    #     instance.save()
    #     return instance
# def encode():
#     model = MenModel('Cross','Content: Жалға беріледі')
#     model_sr = MenSerializer(model)
#     print(model_sr.data, type(model_sr.data), sep='\n')
#     json = JSONRenderer().render(model_sr.data)
#     print(json)
#
# def decode():
#     stream = io.BytesIO(b'{"title":"Cross","content":"Content: jalga"}')
#     data = JSONParser().parse(stream)
#     serializer = MenSerializer(data=data)
#     serializer.is_valid()
#     print(serializer.validated_data)
