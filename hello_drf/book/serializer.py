from rest_framework import serializers
from .models import PeopleInfo

class BookInfoSerializer(serializers.Serializer):
    """图书数据序列化器"""
    id = serializers.IntegerField(label='ID', read_only=True)
    name = serializers.CharField(label='名称', max_length=20)

class PersonInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PeopleInfo
        fields = ('id','name','book')