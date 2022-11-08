from rest_framework import serializers
from .models import BookInfo,PeopleInfo

class BookInfoSerializer(serializers.Serializer):
    """图书数据序列化器"""
    id = serializers.IntegerField(label='ID', read_only=True)
    name = serializers.CharField(label='名称', max_length=20)
    pub_date = serializers.CharField(label='发布时间')
    readcount = serializers.IntegerField(default=1,label='阅读量',max_value=99)
    commentcount = serializers.IntegerField(default=2,label='评论量',min_value=5)
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
    def update(self, instance, validated_data):
        instance.readcount = validated_data.get('readcount',instance.readcount)
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance
class PersonInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PeopleInfo
        # fields = '__all__'
        # fields = ('id','name','book')
        exclude = ('id')