import io

from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from .models import Men


# class MenModel:
#     def __init__(self,title,content):
#         self.title = title
#         self.content = content

class MenSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    content = serializers.CharField()
    slug = serializers.SlugField(max_length=255)
    photo = serializers.ImageField()
    time_create = serializers.DateTimeField(read_only=True)
    time_update = serializers.DateTimeField(read_only=True)
    is_published = serializers.BooleanField(default=True)
    cat = serializers.CharField()
    content1 = serializers.CharField()
    content2 = serializers.CharField()

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
