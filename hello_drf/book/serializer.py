from rest_framework import serializers
from .models import BookInfo,PeopleInfo

class BookInfoSerializer(serializers.Serializer):
    """图书数据序列化器"""
    id = serializers.IntegerField(label='ID', read_only=True)
    name = serializers.CharField(label='名称', max_length=20)
    pub_date = serializers.CharField(label='发布时间')
    readcount = serializers.IntegerField(label='阅读量',max_value=99)
    commentcount = serializers.IntegerField(label='评论量',min_value=5)
    # def validate_name(self,value):
    #     if 'django' not in value.lower():
    #         raise serializers.ValidationError("图书不是关于Django的")
    #     return value
    def validate(self, attrs):
        if attrs['readcount'] > attrs['commentcount']:
            raise serializers.ValidationError('阅读量不能大于评论量')
        return attrs
    def create(self, validated_data):
        return BookInfo.objects.create(**validated_data)

class PersonInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PeopleInfo
        fields = ('id','name','book')