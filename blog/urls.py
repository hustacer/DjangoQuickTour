# encoding:utf-8

from django.conf.urls import url
from . import views

urlpatterns = [
    #将views.py中声明的index视图函数绑定至blog应用的默认地址。
    url(r'^$', views.index, name='index'),
    url(r'^(?P<pageNo>[\d]+)', views.indexInPages, name='indexInPages'),
    url(r'^category/(?P<categoryID>[\d]+)/(?P<pageNo>[\d]+)', views.categoryInPages, name='categoryInPages'),
    url(r'^category/(?P<categoryID>[\d]+)', views.category, name='category'),
    url(r'^article/(?P<articleID>[\d]+)', views.article, name='article'),
]