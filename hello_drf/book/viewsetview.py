
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from django.http import JsonResponse
from .models import BookInfo
from .serializer import BookInfoSerializer

class BooksInfoView(GenericViewSet):

    def list(self,request):
        books = BookInfo.objects.all()
        ser = BookInfoSerializer(books,many=True)
        return Response(ser.data)

    def create(self,request):
        data = request.data
        ser = BookInfoSerializer(data=data)
        ser.is_valid(raise_exception=True)
        ser.save()
        return Response(ser.data)


class BookInfoView(GenericViewSet):

    queryset = BookInfo.objects.all()  # 指定当前类视图使用的查询集数据
    serializer_class = BookInfoSerializer  # 指定当前类视图使用的序列化器
    def retrieve(self,request,pk):
        book = self.get_object()
        ser = BookInfoSerializer(book)
        return Response(ser.data)
    def update(self,request,pk):
        book = BookInfo.get_object()
        ser = BookInfoSerializer(book)
        return Response(ser.data)
    def destroy(self,request,pk):
        book = BookInfo.get_object()
        ser = BookInfoSerializer(book)
        return Response(ser.data)
