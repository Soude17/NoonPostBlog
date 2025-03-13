from django.urls import path,re_path
from .views import article_detail


app_name='blog'
urlpatterns = [
    re_path(r'detail/(?P<slug>[-\w]+)/',article_detail,name='article_detail'),
]
