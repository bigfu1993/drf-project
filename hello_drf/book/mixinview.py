from rest_framework.generics import GenericAPIView
from rest_framework.mixins import CreateModelMixin,DestroyModelMixin,UpdateModelMixin,RetrieveModelMixin,ListModelMixin
from rest_framework.response import Response

from .models import BookInfo
from .serializer import BookInfoSerializer

class BooksInfoView(ListModelMixin,CreateModelMixin,GenericAPIView):
    queryset = BookInfo.objects.all()
    serializer_class = BookInfoSerializer
    def get(self,request):
        return self.list(request)
    def post(self,request):
        return self.create(request)

class BookInfoView(RetrieveModelMixin,UpdateModelMixin,GenericAPIView):
    queryset = BookInfo.objects.all()
    serializer_class = BookInfoSerializer
    def get(self,request,pk):
        return self.retrieve(request,pk)

    def put(self, request, pk):
        return self.update(request, pk)
