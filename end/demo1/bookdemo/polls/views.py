from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, JsonResponse, FileResponse
from .models import *
from django.views.generic import View,TemplateView,ListView,CreateView,DeleteView,UpdateView,DateDetailView as DV
from django.contrib.auth import authenticate, login as lin, logout as lot
from .forms import RegistForm
def index(request):
    print("==========")
    # print(request)
    # print(dir(request))
    # print(request.headers)
    print(request.GET.get('hobbys'))
    print(request.GET.getlist('hobbys'))



    questions = Question.objects.all()
    return render(request, 'polls/index.html', {"questions": questions})

    # return HttpResponse('首页')

def detail(request,qid):
    print(qid, '===')
    if request.method == "GET":
        print('当前用户', request.user.username)
        if request.user and request.user.username != '':
            #已经登陆过了
            print('用户投过票的问题',request.user.questions,type(request.user.questions.all()))
            try:
                question = Question.objects.get(id=qid)
                if question in request.user.questions.all():
                    print('已经投过票')
                    url = reverse('polls:result', args=(qid))
                    return redirect(to=url)

                else:
                    try:
                        # question = Question.objects.get(id=qid)
                        return render(request, 'polls/detail.html', {"question": question})
                    except:
                        return HttpResponse('问题不合法')
                    # return HttpResponse('详情页'+qid)
            except Exception as e:
                print(e,'====')
                return HttpResponse('问题不合法')

        else:
            url = reverse('polls:login')+"?next=/polls/detail/"+qid+'/'
            return redirect(to=url)
    elif request.method == "POST":
        choiceid = request.POST.get('num')
        try:
            choice = Choices.objects.get(id=choiceid)
            choice.votes+=1
            choice.save()

            request.user.questions.add(Question.objects.get(id=qid))

            url = reverse("polls:result", args=(qid,))
            return redirect(to=url)
        except:
            return HttpResponse('选项不合法')



def result(request,qid):
    try:
        question = Question.objects.get(id=qid)
        return render(request,'polls/result.html', {"question":question})
    except:
        return HttpResponse('问题不合法')

# Create your views here.
# class ResultView(View):
#     def get(self,request,qid):
#         try:
#             question = Question.objects.get(id=qid)
#             return render(request,'polls:result.html', {'question:question'})
#         except Exception as e:
#             print(e)
#             return HttpResponse('问题不合法')
def login(request):
    if request.method == 'GET':
        return render(request,'polls/login.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        #可以使用django自带的用户认证系统 认证成功返回用户 失败返回None
        user = authenticate(username=username, password=password)
        if user:
            #调用django登陆方法，其实是为了生成cookie
            lin(request, user)
            next = request.GET.get("next")
            if next:
                url = next

            else:

                url = reverse('polls:index')
            return redirect(to=url)
        else:
            # url = reverse('polls:login')
            # return redirect(to=url)
            return render(request, 'polls/login.html', {'errors': '用户名密码不一致'})


def regist(request):
    if request.method == 'GET':
        # return render(request, 'polls/regist.html')
        rf = RegistForm()
        return render(request,'polls/regist.html', {'rf': rf})
    else:

        rf = RegistForm(request.POST)
        if rf.is_valid():
            print(rf,"++",rf.cleaned_data["username"])


            username = rf.cleaned_data["username"]
            password = rf.cleaned_data["password"]
            password2 = rf.cleaned_data["password2"]
            if User.objects.filter(username=username).count()>0:
                # return HttpResponse("用户名已存在")
                return render(request, 'polls/regist.html',{"errors":"用户名已存在"})
            else:
                if password == password2:
                    # User.objects.create_user(username=username, password=password)
                    rf.save()
                    url = reverse("polls:login")
                    return redirect(to=url)
                else:
                    return render(request, 'polls/regist.html', {"errors": "密码不一致"})
                    # return HttpResponse("密码不一致")
        else:
            return HttpResponse("未知错误")

def logout(request):
    lot(request)
    url = reverse('polls:index')
    return redirect(to=url)