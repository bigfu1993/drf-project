
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from django.http import JsonResponse
from .models import BookInfo
from .serializer import BookInfoSerializer

class BooksInfoView(ViewSet):

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


class BookInfoView(ViewSet):

    def create(self,request):
        books = BookInfo.objects.all()
        ser = BookInfoSerializer(data=books,many=True)
        return Response(ser.data)
