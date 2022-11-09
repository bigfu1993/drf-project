from rest_framework.views import APIView
from rest_framework.response import Response
from .models import BookInfo
from .serializer import BookInfoSerializer


class BooksInfoView(APIView):
    def get(self,request):
        books = BookInfo.objects.all()
        ser = BookInfoSerializer(books,many=True)
        return Response(ser.data)

    def post(selfs,request):
        book = request.data
        ser = BookInfoSerializer(data=book)
        ser.is_valid(raise_exception=True)
        ser.save()
        return Response(ser.data)

class BookInfoView(APIView):
    def get(self,request,book_id):
        book = BookInfo.objects.get(id=book_id)
        ser = BookInfoSerializer(book)
        return Response(ser.data)

    def put(selfs,request,book_id):
        data=request.data
        book = BookInfo.objects.get(id=book_id)
        ser = BookInfoSerializer(book,data=data)
        ser.is_valid()
        # 3、更新数据
        ser.save()
        # 4、返回结果
        return Response(ser.data)


    def delete(selfs,request,pk):
        pass

