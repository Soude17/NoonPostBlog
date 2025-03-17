from django.urls import path,re_path
from .views import article_detail,article_list,category_article,tag_article


app_name='blog'
urlpatterns = [
    re_path(r'detail/(?P<slug>[-\w]+)/',article_detail,name='article_detail'),
    path('article_list/',article_list,name='article_list'),
    re_path(r'category/(?P<slug>[-\w]+)/',category_article,name='category_article'),
    re_path(r'tag/(?P<slug>[-\w]+)/',tag_article,name='tag_article'),
]
