from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from .serializer import BookInfoSerializer
from .models import BookInfo

class BooksInfoView(GenericAPIView):
    queryset = BookInfo.objects.all()
    serializer_class = BookInfoSerializer
    def get(self,request):
        book = self.get_queryset()
        ser = self.get_serializer(book,many=True)
        return Response(ser.data)
    def post(self,request):
        data = request.data
        ser = self.get_serializer(data=data)
        ser.is_valid(raise_exception=True)
        ser.save()
        return Response(ser.data)

class BookInfoView(GenericAPIView):
    queryset = BookInfo.objects.all()
    serializer_class = BookInfoSerializer
    def get(self,request,book_id):
        book = BookInfo.objects.get(id=book_id)
        ser = self.get_serializer(book)
        return Response(ser.data)
    def put(self,request,book_id):
        data = request.data
        book = BookInfo.objects.get(id=book_id)
        ser = self.get_serializer(book,data=data)
        ser.is_valid(raise_exception=True)
        ser.save()
        return  Response(ser.data)