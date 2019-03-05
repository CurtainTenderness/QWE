from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from . import models
from django.shortcuts import redirect,reverse
# Ajax内容引入
from django.views.decorators.http import require_GET,require_POST
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict
from django.core.serializers import serialize

# 事物的导入
from django.db import transaction

# 封装
from . import forms

# Create your views here.
# 主页
def index(request):
    # print('博客')
    # return HttpResponse('博客')
    return render(request,'myblog/index.html',{'msg':'今天真烦'})

# 登录
def login(req):
    if req.method=='GET':
        return render(req,"myblog/login.html",{'msg':'登录页面'})
    elif req.method=='POST':
        name=req.POST.get('name')
        password=req.POST.get('password')
        try:
            models.Users.objects.get(name=name,password=password)
            user=models.Users.objects.get(id=1)
            print(user.name)
            return HttpResponse('登陆成功')
        except:
            return render(req,'myblog/login.html',{'msg':'登陆成功'})

# 注册
def signin(req):
    if req.method == 'GET':
        return render(req, "myblog/signin.html", {'msg': '注册页面'})
    elif req.method== 'POST':
        name = req.POST.get('name')
        password = req.POST.get('password')
        email = req.POST.get('email')
        age = req.POST.get('age')
        try:
            user=models.Users(name=name,password=password,email=email,age=age)
            user.save()
            return render(req,'myblog/login.html',{'msg':'请登录'})
        except:
            return render(req,"myblog/signin.html",{'msg':'注册失败'})




# 确保整个方法具有原子性，事物不能用后台admin打开，需要用网址直接打开
@transaction.atomic()
# 发表文章
def addarticle(req):
    if req.method=='GET':
        # return HttpResponse('chulaimei ')
        return render(req, 'myblog/addarticle.html')
    elif req.method=='POST':
        title=req.POST['title']
        content=req.POST['content']
        user=models.Users.objects.get(pk=1)
        # 设置还原点
        s_id=transaction.savepoint()
        try:
            # 测试时最容易使用的一个错误
            # 1/0
            article=models.Article(title=title,content=content,author=user)
            article.save()
            transaction.savepoint_commit(s_id)
            return HttpResponse('成功')
        except:
            transaction.savepoint_rollback(s_id)
            return HttpResponse('失败')
        # return redirect(reverse('myblog:index'))


