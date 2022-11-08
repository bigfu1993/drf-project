from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse

from django.http import JsonResponse
# Create your views here.
from .models import BookInfo,PeopleInfo
from .serializer import BookInfoSerializer,PersonInfoSerializer

class BooksView(APIView):
    def get(self,request):
        books = BookInfo.objects.all()
        serializer = BookInfoSerializer(books, many=True)
        return Response(serializer.data)


class BookView(APIView):
    def get(self,request,book_id):
        book = BookInfo.objects.get(id=book_id)
        ser = BookInfoSerializer(book)
        return Response(ser.data)
    def post(self,request):
        print(request.data,'000')
        print(request.query_params['key'],'111')
        book = request.data
        ser = BookInfoSerializer(data=book)
        ser.is_valid(raise_exception=True)
        ser.save()
        return Response(ser.data)
    def put(self,request):
        print(request,'000')
        return JsonResponse({'success':'true'})


class PeopleInfoView(APIView):
    def get(self,request):
        peoples = PeopleInfo.objects.all()
        ser = PersonInfoSerializer(peoples,many=True)
        return JsonResponse(ser.data,safe=False)
