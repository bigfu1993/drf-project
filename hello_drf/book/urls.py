from django.conf.urls import url
from . import views,apiview,genericapiview

urlpatterns = [
    # url(r'^books/$', views.BooksView.as_view()),
    # url(r'^book/(?P<book_id>\d+)$', views.BookView.as_view()),
    # url(r'^peoples/$', views.PeopleInfoView.as_view()),
    url(r'^books_apiview/$', apiview.BooksInfoView.as_view()),
    url(r'^books_apiview/(?P<book_id>\d+)$', apiview.BookInfoView.as_view()),
    url(r'^books_genericview/$', genericapiview.BooksInfoView.as_view()),
    url(r'^books_genericview/(?P<book_id>\d+)$', genericapiview.BookInfoView.as_view()),
]