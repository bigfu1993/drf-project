from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.response import Response

from .models import BookInfo
from .serializer import BookInfoSerializer

class BooksInfoView(ListCreateAPIView):
    queryset = BookInfo.objects.all()
    serializer_class = BookInfoSerializer

class BookInfoView(RetrieveUpdateDestroyAPIView):
    queryset = BookInfo.objects.all()
    serializer_class = BookInfoSerializer
