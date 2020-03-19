from django.shortcuts import render
from django.template import loader
from .models import Book, Hero
# Create your views here.
#MVT V 视图模块
#在此处接受请求，处理数据，返回响应
from django.http import HttpResponse
#3.编写对应的视图函数
def index(request):
    # return HttpResponse('这里是首页')
    #1.获取模板
    # templates = loader.get_template('index.html')
    #2.渲染模板数据
    books = Book.objects.all()
    # context = {'books': books}
    # result = templates.render(context)
    #3.将渲染结果使用Httpresponse返回
    # return HttpResponse(result)
    #三合一写法
    return render(request, 'index.html', {'books': books})

def detail(request,bookid):
    # return HttpResponse('这里是详情页'+bookid)
    # templates = loader.get_template('detail.html')
    book = Book.objects.get(id=bookid)
    # context = {'book': book}
    # result = templates.render(context)
    # return HttpResponse(result)
    return render(request, 'detail.html', {'book': book})


def about(request):
    return HttpResponse('这里是关于页面')
#使用django模板
#MVT
