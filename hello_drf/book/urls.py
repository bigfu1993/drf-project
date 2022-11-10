from django.conf.urls import url
from . import views,apiview,genericapiview,mixinview,mulitimixinview,viewsetview

urlpatterns = [
    # url(r'^books/$', views.BooksView.as_view()),
    # url(r'^book/(?P<book_id>\d+)$', views.BookView.as_view()),
    # url(r'^peoples/$', views.PeopleInfoView.as_view()),
    url(r'^books_apiview/$', apiview.BooksInfoView.as_view()),
    url(r'^books_apiview/(?P<book_id>\d+)$', apiview.BookInfoView.as_view()),
    url(r'^books_genericapiview/$', genericapiview.BooksInfoView.as_view()),
    url(r'^books_genericapiview/(?P<book_id>\d+)$', genericapiview.BookInfoView.as_view()),
    url(r'^books_mixinview/$', mixinview.BooksInfoView.as_view()),
    url(r'^books_mixinview/(?P<pk>\d+)$', mixinview.BookInfoView.as_view()),
    url(r'^books_mulitimixinview/$', mulitimixinview.BooksInfoView.as_view()),
    url(r'^books_mulitimixinview/(?P<pk>\d+)$', mulitimixinview.BookInfoView.as_view()),
    url(r'^books_viewsetview/$', viewsetview.BooksInfoView.as_view({'get': 'list', 'post': 'create'})),
    # url(r'^books_viewsetview/(?P<pk>\d+)$', viewsetview.BookInfoView.as_view({'put': 'update','get':'retrieve','delete':'destroy'})),
]