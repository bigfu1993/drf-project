from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from django.http import JsonResponse
# Create your views here.
from .models import BookInfo
from .serializer import BookInfoSerializer

class BooksView(APIView):
    def get(self,request):
        books = BookInfo.objects.all()
        serializer = BookInfoSerializer(books, many=True)
        return Response(serializer.data)



class BookView(APIView):
    def get(self,request):
        print('000')
        id = request.query_params.boo
        book = BookInfo.objects.all(id=id)
        serializer = BookInfoSerializer(book)
        return Response(serializer.data)
