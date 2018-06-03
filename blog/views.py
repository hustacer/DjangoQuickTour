# encoding:utf-8

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from blog.models import *
from django.core.paginator import *

def index(request):
    #loader的get_template函数加载页面模板
    return indexInPages(request, 1)

def article(reqeust, articleID):
    template = loader.get_template('blog/article.html')
    article = Article.objects.get(id=articleID)
    context = {
        'article': article,
    }
    return HttpResponse(template.render(context, reqeust))

def indexInPages(request, pageNo):
    template = loader.get_template('blog/index.html')
    allArticles = Article.objects.all().order_by('-timestamp')
    p = Paginator(allArticles, 5)
    articlesInPage = p.page(pageNo)
    context = {
        'all_articles' : articlesInPage,
    }
    return HttpResponse(template.render(context, request))
