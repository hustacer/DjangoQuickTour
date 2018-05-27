# encoding:utf-8

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader

def index(reqeust):
#    return HttpResponse('''<center><h1>For Fun</h1></center>
#            <span style='font-weight:bold;'>孔子曰:</span><span style='color:gray;'>学而时习之,不亦说乎</span>''')
    #loader的get_template函数加载页面模板
    template = loader.get_template('blog/index.html')
    #声明context字典
    context = {
        'authorName': 'LY',
    }
    return HttpResponse(template.render(context, reqeust))