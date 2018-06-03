# encoding:utf-8

from django.conf.urls import url
from . import views

urlpatterns = [
    #将views.py中声明的index视图函数绑定至blog应用的默认地址。
    url(r'^$', views.index, name='index'),
    url(r'^(?P<pageNo>[\d]+)', views.indexInPages, name='indexInPages'),
    url(r'^article/(?P<articleID>[0-9]+)', views.article, name='article')
]