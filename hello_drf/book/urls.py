from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^books/$', views.BooksView.as_view()),
    # url(r'^book/(?P<book_id>\d+)$', views.BookView.as_view()),
]