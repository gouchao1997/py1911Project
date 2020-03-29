from django.shortcuts import render, redirect, reverse
from django.template import loader
from .models import Book, Hero
# Create your views here.
#MVT V 视图模块
#在此处接受请求，处理数据，返回响应
from django.http import HttpResponse, HttpResponseRedirect
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
def deletebook(request,bookid):
    book = Book.objects.get(id=bookid)
    book.delete()
    # return HttpResponseRedirect('删除成功')
    # return HttpResponseRedirect(redirect_to='/')

    #在view视图里解除硬编码
    url = reverse("booktest:index")
    return redirect(to=url)
def deletehero(request,heroid):
    hero = Hero.objects.get(id=heroid)
    bookid = hero.book.id
    hero.delete()
    url = reverse("booktest:detail", args=(bookid,))
    return redirect(to=url)
def addhero(request,bookid):
    #视图函数中可以同时存在get和post请求，默认为get
    if request.method == "GET":
        return render(request,'addhero.html')
    elif request.method =="POST":
        hero = Hero()
        hero.name = request.POST.get("heroname")
        hero.content = request.POST.get("herocontent")
        hero.gender = request.POST.get("sex")
        hero.book = Book.objects.get(id=bookid)
        hero.save()
        url = reverse("booktest:detail",args=(bookid,))
        return redirect(to=url)
def edithero(request,heroid):
    hero = Hero.objects.get(id=heroid)
    if request.method == 'GET':
        return render(request,'edithero.html',{"hero": hero})
    elif request.method == 'POST':
        hero.name = request.POST.get("heroname")
        hero.content = request.POST.get("herocontent")
        hero.gender = request.POST.get("sex")
        hero.save()
        url = reverse("booktest:detail",args=(hero.book.id,))
        return redirect(to=url)

def about(request):
    return HttpResponse('这里是关于页面')
#使用django模板
#MVT
