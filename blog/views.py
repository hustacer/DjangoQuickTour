# encoding:utf-8

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from blog.models import *
from django.core.paginator import *
from django.shortcuts import get_object_or_404

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

def categoryInPages(request, categoryID, pageNo):
    template = loader.get_template('blog/index.html')
    cat = get_object_or_404(Category, id=categoryID)
    categories = Category.objects.all();

    articlesInCat = Article.objects.filter(category=categoryID).order_by('-timestamp')
    p = Paginator(articlesInCat, 5)
    articlesInPage = p.page(pageNo)

    context = {
        'cat' : cat,
        'articles': articlesInPage,
        'categories' : categories,
    }
    return HttpResponse(template.render(context, request))

def category(request, categoryID):
    return categoryInPages(request, categoryID, 1)